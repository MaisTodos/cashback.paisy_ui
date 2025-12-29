from typing import List, Optional

from ..core import PUIComponentABC
from ..mixins import PUIVariantMixin
from ..utils import add_css, parse_html


class PUIInputABC(PUIComponentABC):
    """<fieldset class="fieldset rounded-box w-full border border-base-300 p-4 validator">
    </fieldset>
    """

    _input_type: str

    @property
    def legend(self):
        _legend = self.find("legend")
        return _legend

    @property
    def input(self):
        _input = self.find("input")
        return _input

    @property
    def label(self):
        _label = self.find("label")
        return _label

    @property
    def disabled(self):
        self.input.attrs.update(disabled="true")
        return self

    def __init__(
        self,
        *classes,
        name: str,
        id: str,
        pattern: Optional[str] = None,
        validator_hint: Optional[str] = None,
        label: Optional[str] = None,
        legend: Optional[str] = None,
        **attributes,
    ):
        super().__init__(*classes)
        if legend:
            _legend, _ = parse_html(
                f'<legend class="fieldset-legend">{legend}</legend>'
            )
            self.tag.append(_legend)

        _input, _ = parse_html("<input/>")
        _label, _ = parse_html(f"<label></label>")
        _label.append(_input)

        if label:
            add_css(_label, "label")
            _label.append(label)
        else:
            add_css(_label, "validator", "w-full")

        if not self._input_type in ["range", "checkbox", "radio", "file"]:
            add_css(_input if label else _label, "input")

        self.tag.append(_label)

        if validator_hint:
            _hint, _ = parse_html(f'<p class="validator-hint">{validator_hint}</p>')
            self.tag.append(_hint)
        self.input.attrs.update(name=name, id=id, type=self._input_type, **attributes)
        if pattern:
            self.input.attrs.update(pattern=pattern)

        self.post_init()

    def post_init(self):
        pass


class PUICheckbox(PUIInputABC):
    __doc__ = PUIInputABC.__doc__
    _input_type = "checkbox"

    def post_init(self):
        add_css(self.input, "checkbox")


class PUIFileInput(PUIInputABC, PUIVariantMixin):
    __doc__ = PUIInputABC.__doc__
    _input_type = "file"
    _variant_prefix = "file-input"

    def post_init(self):
        add_css(self.input, "file-input")

    @property
    def xs(self):
        add_css(self.input, "file-input-xs")
        return self

    @property
    def sm(self):
        add_css(self.input, "file-input-sm")
        return self

    @property
    def md(self):
        add_css(self.input, "file-input-md")
        return self

    @property
    def lg(self):
        add_css(self.input, "file-input-lg")
        return self

    @property
    def xl(self):
        add_css(self.input, "file-input-xl")
        return self


class PUIFilter(PUIComponentABC):
    """
    <div class="filter">
        <input class="btn filter-reset" type="radio" aria-label="x"/>
        [[content]]
    </div>
    """

    @property
    def reset_input(self):
        _input = self.find("input", {"class": "filter-reset"})
        return _input

    def __init__(self, *classes, name: str, id: str, options: List[str], **attributes):
        super().__init__(*classes, **attributes)
        self.reset_input.attrs.update(name=name, id=id)
        for option in options:
            _input, _ = parse_html(
                f'<input class="btn" type="radio" name="{name}" aria-label="{option}"/>'
            )
            self.wrapper.append(_input)


class PUIRadio(PUIInputABC, PUIVariantMixin):
    __doc__ = PUIInputABC.__doc__
    _input_type = "radio"
    _variant_prefix = "radio"

    def post_init(self):
        add_css(self.input, "radio")


class PUIToggle(PUIInputABC, PUIVariantMixin):
    __doc__ = PUIInputABC.__doc__
    _input_type = "checkbox"
    _variant_prefix = "toggle"

    def post_init(self):
        add_css(self.input, "toggle")


class PUIRange(PUIInputABC, PUIVariantMixin):
    __doc__ = PUIInputABC.__doc__
    _input_type = "range"
    _variant_prefix = "range"

    # TODO: Size variants

    def post_init(self):
        add_css(self.input, "range")


# TODO: Implement
# class PUIRating(PUIComponentABC):
#     pass


class PUISelect(PUIComponentABC):
    __doc__ = PUIInputABC.__doc__

    def __init__(
        self,
        *classes,
        name: str,
        id: str,
        options: List[str],
        label: str | None = None,
        legend: str | None = None,
        **attributes,
    ):
        super().__init__(*classes, **attributes)
        if legend:
            _legend, _ = parse_html(
                f'<legend class="fieldset-legend">{legend}</legend>'
            )
            self.tag.append(_legend)

        if label:
            _label, _ = parse_html(
                f'<label class="label"><select class="select w-full"></select>{label}</label>'
            )
            self.tag.append(_label)
        else:
            _input, _ = parse_html('<select class="select w-full"></select>')
            self.tag.append(_input)

        self.input.attrs.update(name=name, id=id)
        for option in options:
            _option, _ = parse_html(f"<option>{option}</option>")
            self.input.append(_option)

    @property
    def input(self):
        _input = self.find("select")
        return _input

    @property
    def disabled(self):
        self.input.attrs.update(disabled="true")
        return self


class PUITextInput(PUIInputABC, PUIVariantMixin):
    __doc__ = PUIInputABC.__doc__
    _input_type = "text"
    _variant_prefix = "input"

    def __init__(
        self,
        *classes,
        name: str,
        id: str,
        datalist: List[str] = [],
        pattern: Optional[str] = None,
        validator_hint: Optional[str] = None,
        label: str | None = None,
        legend: str | None = None,
        **attributes,
    ):
        super().__init__(
            *classes,
            name=name,
            id=id,
            label=label,
            legend=legend,
            pattern=pattern,
            validator_hint=validator_hint,
            **attributes,
        )
        if datalist:
            _datalist_id = f"{id}-datalist"
            _datalist, _ = parse_html(f'<datalist id="{_datalist_id}"></datalist>')
            for option in datalist:
                _option, _ = parse_html(f'<option value="{option}"></option>')
                _datalist.append(_option)
            self.tag.append(_datalist)
            self.input.attrs.update(list=_datalist_id)


class PUIDateInput(PUIInputABC, PUIVariantMixin):
    __doc__ = PUIInputABC.__doc__
    _input_type = "date"
    _variant_prefix = "input"


class PUITimeInput(PUIInputABC, PUIVariantMixin):
    __doc__ = PUIInputABC.__doc__
    _input_type = "time"
    _variant_prefix = "input"


class PUIDateTimeLocalInput(PUIInputABC, PUIVariantMixin):
    __doc__ = PUIInputABC.__doc__
    _input_type = "datetime-local"
    _variant_prefix = "input"


class PUISearchInput(PUIInputABC, PUIVariantMixin):
    __doc__ = PUIInputABC.__doc__
    _input_type = "search"
    _variant_prefix = "input"


class PUIEmailInput(PUIInputABC, PUIVariantMixin):
    __doc__ = PUIInputABC.__doc__
    _input_type = "email"
    _variant_prefix = "input"


class PUIPasswordInput(PUIInputABC, PUIVariantMixin):
    __doc__ = PUIInputABC.__doc__
    _input_type = "password"
    _variant_prefix = "input"


class PUINumberInput(PUIInputABC, PUIVariantMixin):
    __doc__ = PUIInputABC.__doc__
    _input_type = "number"
    _variant_prefix = "input"


class PUITelephoneInput(PUIInputABC, PUIVariantMixin):
    __doc__ = PUIInputABC.__doc__
    _input_type = "tel"
    _variant_prefix = "input"


class PUIUrlInput(PUIInputABC, PUIVariantMixin):
    __doc__ = PUIInputABC.__doc__
    _input_type = "url"
    _variant_prefix = "input"
