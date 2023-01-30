<html lang="en" style="--main-padding-y:74px; --top_bar-height:51px;"><head><style id="error_marker.css">
    .error_widget_wrapper {
        background: inherit;
        color: inherit;
        border:none
    }
    .error_widget {
        border-top: solid 2px;
        border-bottom: solid 2px;
        margin: 5px 0;
        padding: 10px 40px;
        white-space: pre-wrap;
    }
    .error_widget.ace_error, .error_widget_arrow.ace_error{
        border-color: #ff5a5a
    }
    .error_widget.ace_warning, .error_widget_arrow.ace_warning{
        border-color: #F1D817
    }
    .error_widget.ace_info, .error_widget_arrow.ace_info{
        border-color: #5a5a5a
    }
    .error_widget.ace_ok, .error_widget_arrow.ace_ok{
        border-color: #5aaa5a
    }
    .error_widget_arrow {
        position: absolute;
        border: solid 5px;
        border-top-color: transparent!important;
        border-right-color: transparent!important;
        border-left-color: transparent!important;
        top: -5px;
    }

/*# sourceURL=ace/css/error_marker.css */</style><style id="ace-tm">.ace-tm .ace_gutter {
  background: #f0f0f0;
  color: #333;
}

.ace-tm .ace_print-margin {
  width: 1px;
  background: #e8e8e8;
}

.ace-tm .ace_fold {
    background-color: #6B72E6;
}

.ace-tm {
  background-color: #FFFFFF;
  color: black;
}

.ace-tm .ace_cursor {
  color: black;
}
        
.ace-tm .ace_invisible {
  color: rgb(191, 191, 191);
}

.ace-tm .ace_storage,
.ace-tm .ace_keyword {
  color: blue;
}

.ace-tm .ace_constant {
  color: rgb(197, 6, 11);
}

.ace-tm .ace_constant.ace_buildin {
  color: rgb(88, 72, 246);
}

.ace-tm .ace_constant.ace_language {
  color: rgb(88, 92, 246);
}

.ace-tm .ace_constant.ace_library {
  color: rgb(6, 150, 14);
}

.ace-tm .ace_invalid {
  background-color: rgba(255, 0, 0, 0.1);
  color: red;
}

.ace-tm .ace_support.ace_function {
  color: rgb(60, 76, 114);
}

.ace-tm .ace_support.ace_constant {
  color: rgb(6, 150, 14);
}

.ace-tm .ace_support.ace_type,
.ace-tm .ace_support.ace_class {
  color: rgb(109, 121, 222);
}

.ace-tm .ace_keyword.ace_operator {
  color: rgb(104, 118, 135);
}

.ace-tm .ace_string {
  color: rgb(3, 106, 7);
}

.ace-tm .ace_comment {
  color: rgb(76, 136, 107);
}

.ace-tm .ace_comment.ace_doc {
  color: rgb(0, 102, 255);
}

.ace-tm .ace_comment.ace_doc.ace_tag {
  color: rgb(128, 159, 191);
}

.ace-tm .ace_constant.ace_numeric {
  color: rgb(0, 0, 205);
}

.ace-tm .ace_variable {
  color: rgb(49, 132, 149);
}

.ace-tm .ace_xml-pe {
  color: rgb(104, 104, 91);
}

.ace-tm .ace_entity.ace_name.ace_function {
  color: #0000A2;
}


.ace-tm .ace_heading {
  color: rgb(12, 7, 255);
}

.ace-tm .ace_list {
  color:rgb(185, 6, 144);
}

.ace-tm .ace_meta.ace_tag {
  color:rgb(0, 22, 142);
}

.ace-tm .ace_string.ace_regex {
  color: rgb(255, 0, 0)
}

.ace-tm .ace_marker-layer .ace_selection {
  background: rgb(181, 213, 255);
}
.ace-tm.ace_multiselect .ace_selection.ace_start {
  box-shadow: 0 0 3px 0px white;
}
.ace-tm .ace_marker-layer .ace_step {
  background: rgb(252, 255, 0);
}

.ace-tm .ace_marker-layer .ace_stack {
  background: rgb(164, 229, 101);
}

.ace-tm .ace_marker-layer .ace_bracket {
  margin: -1px 0 0 -1px;
  border: 1px solid rgb(192, 192, 192);
}

.ace-tm .ace_marker-layer .ace_active-line {
  background: rgba(0, 0, 0, 0.07);
}

.ace-tm .ace_gutter-active-line {
    background-color : #dcdcdc;
}

.ace-tm .ace_marker-layer .ace_selected-word {
  background: rgb(250, 250, 255);
  border: 1px solid rgb(200, 200, 250);
}

.ace-tm .ace_indent-guide {
  background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;
}

.ace-tm .ace_indent-guide-active {
  background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAAAZSURBVHjaYvj///9/hivKyv8BAAAA//8DACLqBhbvk+/eAAAAAElFTkSuQmCC") right repeat-y;
}

/*# sourceURL=ace/css/ace-tm */</style><style id="ace_editor.css">/*
styles = []
for (var i = 1; i < 16; i++) {
    styles.push(".ace_br" + i + "{" + (
        ["top-left", "top-right", "bottom-right", "bottom-left"]
    ).map(function(x, j) {
        return i & (1<<j) ? "border-" + x + "-radius: 3px;" : "" 
    }).filter(Boolean).join(" ") + "}")
}
styles.join("\n")
*/
.ace_br1 {border-top-left-radius    : 3px;}
.ace_br2 {border-top-right-radius   : 3px;}
.ace_br3 {border-top-left-radius    : 3px; border-top-right-radius:    3px;}
.ace_br4 {border-bottom-right-radius: 3px;}
.ace_br5 {border-top-left-radius    : 3px; border-bottom-right-radius: 3px;}
.ace_br6 {border-top-right-radius   : 3px; border-bottom-right-radius: 3px;}
.ace_br7 {border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px;}
.ace_br8 {border-bottom-left-radius : 3px;}
.ace_br9 {border-top-left-radius    : 3px; border-bottom-left-radius:  3px;}
.ace_br10{border-top-right-radius   : 3px; border-bottom-left-radius:  3px;}
.ace_br11{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-left-radius:  3px;}
.ace_br12{border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}
.ace_br13{border-top-left-radius    : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}
.ace_br14{border-top-right-radius   : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}
.ace_br15{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;}


.ace_editor {
    position: relative;
    overflow: hidden;
    padding: 0;
    font: 12px/normal 'Monaco', 'Menlo', 'Ubuntu Mono', 'Consolas', 'source-code-pro', monospace;
    direction: ltr;
    text-align: left;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}

.ace_scroller {
    position: absolute;
    overflow: hidden;
    top: 0;
    bottom: 0;
    background-color: inherit;
    -ms-user-select: none;
    -moz-user-select: none;
    -webkit-user-select: none;
    user-select: none;
    cursor: text;
}

.ace_content {
    position: absolute;
    box-sizing: border-box;
    min-width: 100%;
    contain: style size layout;
    font-variant-ligatures: no-common-ligatures;
}

.ace_dragging .ace_scroller:before{
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    content: '';
    background: rgba(250, 250, 250, 0.01);
    z-index: 1000;
}
.ace_dragging.ace_dark .ace_scroller:before{
    background: rgba(0, 0, 0, 0.01);
}

.ace_gutter {
    position: absolute;
    overflow : hidden;
    width: auto;
    top: 0;
    bottom: 0;
    left: 0;
    cursor: default;
    z-index: 4;
    -ms-user-select: none;
    -moz-user-select: none;
    -webkit-user-select: none;
    user-select: none;
    contain: style size layout;
}

.ace_gutter-active-line {
    position: absolute;
    left: 0;
    right: 0;
}

.ace_scroller.ace_scroll-left {
    box-shadow: 17px 0 16px -16px rgba(0, 0, 0, 0.4) inset;
}

.ace_gutter-cell {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    padding-left: 19px;
    padding-right: 6px;
    background-repeat: no-repeat;
}

.ace_gutter-cell.ace_error {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAABOFBMVEX/////////QRswFAb/Ui4wFAYwFAYwFAaWGAfDRymzOSH/PxswFAb/SiUwFAYwFAbUPRvjQiDllog5HhHdRybsTi3/Tyv9Tir+Syj/UC3////XurebMBIwFAb/RSHbPx/gUzfdwL3kzMivKBAwFAbbvbnhPx66NhowFAYwFAaZJg8wFAaxKBDZurf/RB6mMxb/SCMwFAYwFAbxQB3+RB4wFAb/Qhy4Oh+4QifbNRcwFAYwFAYwFAb/QRzdNhgwFAYwFAbav7v/Uy7oaE68MBK5LxLewr/r2NXewLswFAaxJw4wFAbkPRy2PyYwFAaxKhLm1tMwFAazPiQwFAaUGAb/QBrfOx3bvrv/VC/maE4wFAbRPBq6MRO8Qynew8Dp2tjfwb0wFAbx6eju5+by6uns4uH9/f36+vr/GkHjAAAAYnRSTlMAGt+64rnWu/bo8eAA4InH3+DwoN7j4eLi4xP99Nfg4+b+/u9B/eDs1MD1mO7+4PHg2MXa347g7vDizMLN4eG+Pv7i5evs/v79yu7S3/DV7/498Yv24eH+4ufQ3Ozu/v7+y13sRqwAAADLSURBVHjaZc/XDsFgGIBhtDrshlitmk2IrbHFqL2pvXf/+78DPokj7+Fz9qpU/9UXJIlhmPaTaQ6QPaz0mm+5gwkgovcV6GZzd5JtCQwgsxoHOvJO15kleRLAnMgHFIESUEPmawB9ngmelTtipwwfASilxOLyiV5UVUyVAfbG0cCPHig+GBkzAENHS0AstVF6bacZIOzgLmxsHbt2OecNgJC83JERmePUYq8ARGkJx6XtFsdddBQgZE2nPR6CICZhawjA4Fb/chv+399kfR+MMMDGOQAAAABJRU5ErkJggg==");
    background-repeat: no-repeat;
    background-position: 2px center;
}

.ace_gutter-cell.ace_warning {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAmVBMVEX///8AAAD///8AAAAAAABPSzb/5sAAAAB/blH/73z/ulkAAAAAAAD85pkAAAAAAAACAgP/vGz/rkDerGbGrV7/pkQICAf////e0IsAAAD/oED/qTvhrnUAAAD/yHD/njcAAADuv2r/nz//oTj/p064oGf/zHAAAAA9Nir/tFIAAAD/tlTiuWf/tkIAAACynXEAAAAAAAAtIRW7zBpBAAAAM3RSTlMAABR1m7RXO8Ln31Z36zT+neXe5OzooRDfn+TZ4p3h2hTf4t3k3ucyrN1K5+Xaks52Sfs9CXgrAAAAjklEQVR42o3PbQ+CIBQFYEwboPhSYgoYunIqqLn6/z8uYdH8Vmdnu9vz4WwXgN/xTPRD2+sgOcZjsge/whXZgUaYYvT8QnuJaUrjrHUQreGczuEafQCO/SJTufTbroWsPgsllVhq3wJEk2jUSzX3CUEDJC84707djRc5MTAQxoLgupWRwW6UB5fS++NV8AbOZgnsC7BpEAAAAABJRU5ErkJggg==");
    background-position: 2px center;
}

.ace_gutter-cell.ace_info {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAAAAAA6mKC9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAJ0Uk5TAAB2k804AAAAPklEQVQY02NgIB68QuO3tiLznjAwpKTgNyDbMegwisCHZUETUZV0ZqOquBpXj2rtnpSJT1AEnnRmL2OgGgAAIKkRQap2htgAAAAASUVORK5CYII=");
    background-position: 2px center;
}
.ace_dark .ace_gutter-cell.ace_info {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAAJFBMVEUAAAChoaGAgIAqKiq+vr6tra1ZWVmUlJSbm5s8PDxubm56enrdgzg3AAAAAXRSTlMAQObYZgAAAClJREFUeNpjYMAPdsMYHegyJZFQBlsUlMFVCWUYKkAZMxZAGdxlDMQBAG+TBP4B6RyJAAAAAElFTkSuQmCC");
}

.ace_scrollbar {
    contain: strict;
    position: absolute;
    right: 0;
    bottom: 0;
    z-index: 6;
}

.ace_scrollbar-inner {
    position: absolute;
    cursor: text;
    left: 0;
    top: 0;
}

.ace_scrollbar-v{
    overflow-x: hidden;
    overflow-y: scroll;
    top: 0;
}

.ace_scrollbar-h {
    overflow-x: scroll;
    overflow-y: hidden;
    left: 0;
}

.ace_print-margin {
    position: absolute;
    height: 100%;
}

.ace_text-input {
    position: absolute;
    z-index: 0;
    width: 0.5em;
    height: 1em;
    opacity: 0;
    background: transparent;
    -moz-appearance: none;
    appearance: none;
    border: none;
    resize: none;
    outline: none;
    overflow: hidden;
    font: inherit;
    padding: 0 1px;
    margin: 0 -1px;
    contain: strict;
    -ms-user-select: text;
    -moz-user-select: text;
    -webkit-user-select: text;
    user-select: text;
    /*with `pre-line` chrome inserts &nbsp; instead of space*/
    white-space: pre!important;
}
.ace_text-input.ace_composition {
    background: transparent;
    color: inherit;
    z-index: 1000;
    opacity: 1;
}
.ace_composition_placeholder { color: transparent }
.ace_composition_marker { 
    border-bottom: 1px solid;
    position: absolute;
    border-radius: 0;
    margin-top: 1px;
}

[ace_nocontext=true] {
    transform: none!important;
    filter: none!important;
    clip-path: none!important;
    mask : none!important;
    contain: none!important;
    perspective: none!important;
    mix-blend-mode: initial!important;
    z-index: auto;
}

.ace_layer {
    z-index: 1;
    position: absolute;
    overflow: hidden;
    /* workaround for chrome bug https://github.com/ajaxorg/ace/issues/2312*/
    word-wrap: normal;
    white-space: pre;
    height: 100%;
    width: 100%;
    box-sizing: border-box;
    /* setting pointer-events: auto; on node under the mouse, which changes
        during scroll, will break mouse wheel scrolling in Safari */
    pointer-events: none;
}

.ace_gutter-layer {
    position: relative;
    width: auto;
    text-align: right;
    pointer-events: auto;
    height: 1000000px;
    contain: style size layout;
}

.ace_text-layer {
    font: inherit !important;
    position: absolute;
    height: 1000000px;
    width: 1000000px;
    contain: style size layout;
}

.ace_text-layer > .ace_line, .ace_text-layer > .ace_line_group {
    contain: style size layout;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
}

.ace_hidpi .ace_text-layer,
.ace_hidpi .ace_gutter-layer,
.ace_hidpi .ace_content,
.ace_hidpi .ace_gutter {
    contain: strict;
    will-change: transform;
}
.ace_hidpi .ace_text-layer > .ace_line, 
.ace_hidpi .ace_text-layer > .ace_line_group {
    contain: strict;
}

.ace_cjk {
    display: inline-block;
    text-align: center;
}

.ace_cursor-layer {
    z-index: 4;
}

.ace_cursor {
    z-index: 4;
    position: absolute;
    box-sizing: border-box;
    border-left: 2px solid;
    /* workaround for smooth cursor repaintng whole screen in chrome */
    transform: translatez(0);
}

.ace_multiselect .ace_cursor {
    border-left-width: 1px;
}

.ace_slim-cursors .ace_cursor {
    border-left-width: 1px;
}

.ace_overwrite-cursors .ace_cursor {
    border-left-width: 0;
    border-bottom: 1px solid;
}

.ace_hidden-cursors .ace_cursor {
    opacity: 0.2;
}

.ace_hasPlaceholder .ace_hidden-cursors .ace_cursor {
    opacity: 0;
}

.ace_smooth-blinking .ace_cursor {
    transition: opacity 0.18s;
}

.ace_animate-blinking .ace_cursor {
    animation-duration: 1000ms;
    animation-timing-function: step-end;
    animation-name: blink-ace-animate;
    animation-iteration-count: infinite;
}

.ace_animate-blinking.ace_smooth-blinking .ace_cursor {
    animation-duration: 1000ms;
    animation-timing-function: ease-in-out;
    animation-name: blink-ace-animate-smooth;
}
    
@keyframes blink-ace-animate {
    from, to { opacity: 1; }
    60% { opacity: 0; }
}

@keyframes blink-ace-animate-smooth {
    from, to { opacity: 1; }
    45% { opacity: 1; }
    60% { opacity: 0; }
    85% { opacity: 0; }
}

.ace_marker-layer .ace_step, .ace_marker-layer .ace_stack {
    position: absolute;
    z-index: 3;
}

.ace_marker-layer .ace_selection {
    position: absolute;
    z-index: 5;
}

.ace_marker-layer .ace_bracket {
    position: absolute;
    z-index: 6;
}

.ace_marker-layer .ace_error_bracket {
    position: absolute;
    border-bottom: 1px solid #DE5555;
    border-radius: 0;
}

.ace_marker-layer .ace_active-line {
    position: absolute;
    z-index: 2;
}

.ace_marker-layer .ace_selected-word {
    position: absolute;
    z-index: 4;
    box-sizing: border-box;
}

.ace_line .ace_fold {
    box-sizing: border-box;

    display: inline-block;
    height: 11px;
    margin-top: -2px;
    vertical-align: middle;

    background-image:
        url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),
        url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACJJREFUeNpi+P//fxgTAwPDBxDxD078RSX+YeEyDFMCIMAAI3INmXiwf2YAAAAASUVORK5CYII=");
    background-repeat: no-repeat, repeat-x;
    background-position: center center, top left;
    color: transparent;

    border: 1px solid black;
    border-radius: 2px;

    cursor: pointer;
    pointer-events: auto;
}

.ace_dark .ace_fold {
}

.ace_fold:hover{
    background-image:
        url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),
        url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACBJREFUeNpi+P//fz4TAwPDZxDxD5X4i5fLMEwJgAADAEPVDbjNw87ZAAAAAElFTkSuQmCC");
}

.ace_tooltip {
    background-color: #FFF;
    background-image: linear-gradient(to bottom, transparent, rgba(0, 0, 0, 0.1));
    border: 1px solid gray;
    border-radius: 1px;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
    color: black;
    max-width: 100%;
    padding: 3px 4px;
    position: fixed;
    z-index: 999999;
    box-sizing: border-box;
    cursor: default;
    white-space: pre;
    word-wrap: break-word;
    line-height: normal;
    font-style: normal;
    font-weight: normal;
    letter-spacing: normal;
    pointer-events: none;
}

.ace_folding-enabled > .ace_gutter-cell {
    padding-right: 13px;
}

.ace_fold-widget {
    box-sizing: border-box;

    margin: 0 -12px 0 1px;
    display: none;
    width: 11px;
    vertical-align: top;

    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42mWKsQ0AMAzC8ixLlrzQjzmBiEjp0A6WwBCSPgKAXoLkqSot7nN3yMwR7pZ32NzpKkVoDBUxKAAAAABJRU5ErkJggg==");
    background-repeat: no-repeat;
    background-position: center;

    border-radius: 3px;
    
    border: 1px solid transparent;
    cursor: pointer;
}

.ace_folding-enabled .ace_fold-widget {
    display: inline-block;   
}

.ace_fold-widget.ace_end {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42m3HwQkAMAhD0YzsRchFKI7sAikeWkrxwScEB0nh5e7KTPWimZki4tYfVbX+MNl4pyZXejUO1QAAAABJRU5ErkJggg==");
}

.ace_fold-widget.ace_closed {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAGCAYAAAAG5SQMAAAAOUlEQVR42jXKwQkAMAgDwKwqKD4EwQ26sSOkVWjgIIHAzPiCgaqiqnJHZnKICBERHN194O5b9vbLuAVRL+l0YWnZAAAAAElFTkSuQmCCXA==");
}

.ace_fold-widget:hover {
    border: 1px solid rgba(0, 0, 0, 0.3);
    background-color: rgba(255, 255, 255, 0.2);
    box-shadow: 0 1px 1px rgba(255, 255, 255, 0.7);
}

.ace_fold-widget:active {
    border: 1px solid rgba(0, 0, 0, 0.4);
    background-color: rgba(0, 0, 0, 0.05);
    box-shadow: 0 1px 1px rgba(255, 255, 255, 0.8);
}
/**
 * Dark version for fold widgets
 */
.ace_dark .ace_fold-widget {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHklEQVQIW2P4//8/AzoGEQ7oGCaLLAhWiSwB146BAQCSTPYocqT0AAAAAElFTkSuQmCC");
}
.ace_dark .ace_fold-widget.ace_end {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAH0lEQVQIW2P4//8/AxQ7wNjIAjDMgC4AxjCVKBirIAAF0kz2rlhxpAAAAABJRU5ErkJggg==");
}
.ace_dark .ace_fold-widget.ace_closed {
    background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAFCAYAAACAcVaiAAAAHElEQVQIW2P4//+/AxAzgDADlOOAznHAKgPWAwARji8UIDTfQQAAAABJRU5ErkJggg==");
}
.ace_dark .ace_fold-widget:hover {
    box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);
    background-color: rgba(255, 255, 255, 0.1);
}
.ace_dark .ace_fold-widget:active {
    box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);
}

.ace_inline_button {
    border: 1px solid lightgray;
    display: inline-block;
    margin: -1px 8px;
    padding: 0 5px;
    pointer-events: auto;
    cursor: pointer;
}
.ace_inline_button:hover {
    border-color: gray;
    background: rgba(200,200,200,0.2);
    display: inline-block;
    pointer-events: auto;
}

.ace_fold-widget.ace_invalid {
    background-color: #FFB4B4;
    border-color: #DE5555;
}

.ace_fade-fold-widgets .ace_fold-widget {
    transition: opacity 0.4s ease 0.05s;
    opacity: 0;
}

.ace_fade-fold-widgets:hover .ace_fold-widget {
    transition: opacity 0.05s ease 0.05s;
    opacity:1;
}

.ace_underline {
    text-decoration: underline;
}

.ace_bold {
    font-weight: bold;
}

.ace_nobold .ace_bold {
    font-weight: normal;
}

.ace_italic {
    font-style: italic;
}


.ace_error-marker {
    background-color: rgba(255, 0, 0,0.2);
    position: absolute;
    z-index: 9;
}

.ace_highlight-marker {
    background-color: rgba(255, 255, 0,0.2);
    position: absolute;
    z-index: 8;
}

.ace_mobile-menu {
    position: absolute;
    line-height: 1.5;
    border-radius: 4px;
    -ms-user-select: none;
    -moz-user-select: none;
    -webkit-user-select: none;
    user-select: none;
    background: white;
    box-shadow: 1px 3px 2px grey;
    border: 1px solid #dcdcdc;
    color: black;
}
.ace_dark > .ace_mobile-menu {
    background: #333;
    color: #ccc;
    box-shadow: 1px 3px 2px grey;
    border: 1px solid #444;

}
.ace_mobile-button {
    padding: 2px;
    cursor: pointer;
    overflow: hidden;
}
.ace_mobile-button:hover {
    background-color: #eee;
    opacity:1;
}
.ace_mobile-button:active {
    background-color: #ddd;
}

.ace_placeholder {
    font-family: arial;
    transform: scale(0.9);
    transform-origin: left;
    white-space: pre;
    opacity: 0.7;
    margin: 0 10px;
}
/*# sourceURL=ace/css/ace_editor.css */</style><style id="ace_scrollbar.css">.ace_editor>.ace_sb-v div, .ace_editor>.ace_sb-h div{
  position: absolute;
  background: rgba(128, 128, 128, 0.6);
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  border: 1px solid #bbb;
  border-radius: 2px;
  z-index: 8;
}
.ace_editor>.ace_sb-v, .ace_editor>.ace_sb-h {
  position: absolute;
  z-index: 6;
  background: none;
  overflow: hidden!important;
}
.ace_editor>.ace_sb-v {
  z-index: 6;
  right: 0;
  top: 0;
  width: 12px;
}
.ace_editor>.ace_sb-v div {
  z-index: 8;
  right: 0;
  width: 100%;
}
.ace_editor>.ace_sb-h {
  bottom: 0;
  left: 0;
  height: 12px;
}
.ace_editor>.ace_sb-h div {
  bottom: 0;
  height: 100%;
}
.ace_editor>.ace_sb_grabbed {
  z-index: 8;
  background: #000;
}
/*# sourceURL=ace/css/ace_scrollbar.css */</style>
    <!-- Load sentry as early as possible -->
        <script src="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/@sentry/browser/build/bundle.es6.min.js"></script>
    <script>
        Sentry.init({
            dsn: "https://1ad5e9767ad243d396a93ef40135e743:0f66eac85d88443baa349f5bc2497f28@sentry.io/271015",
            release: "a4d84a299dfd728052d336d5620721238079423e",
            environment: "edu",
            whitelistUrls: [
                /https?:\/\/open\.kattis\.com/             ],
            ignoreErrors: [
                "Non-Error exception captured", // Ignoring per https://forum.sentry.io/t/unhandledrejection-non-error-promise-rejection-captured-with-value/14062/16
                "Non-Error promise rejection captured", // Ignoring per https://forum.sentry.io/t/unhandledrejection-non-error-promise-rejection-captured-with-value/14062/16
                'ResizeObserver loop limit exceeded' // Ignoring per https://github.com/WICG/resize-observer/issues/38#issuecomment-493014026
            ],
            autoSessionTracking: false        });
                    Sentry.setUser({
                username: "saifur-rahman2",
                                    email: "msaifur92@gmail.com",
                            })
            </script>

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Add Two Numbers – Kattis, Kattis</title>

    <!-- Jquery and Jquery-ui -->
    <link href="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/jquery-ui-dist/jquery-ui.theme.min.css" rel="stylesheet">
    <script src="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/jquery/dist/jquery.min.js"></script>
    <script src="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/jquery-ui-dist/jquery-ui.min.js"></script>

    <!-- Timezone Cookie -->
    <script type="module" src="/js/8cb58e4951798a7fc78fad722dc252f7/modules/timezone.js"></script>

    <!-- Fonts/Icons -->
    <link href="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/@fortawesome/fontawesome-free/css/all.min.css" rel="stylesheet">

            <link href="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/@fontsource/merriweather/300.css" rel="stylesheet">
        <link href="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/@fontsource/merriweather/300-italic.css" rel="stylesheet">
            <link href="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/@fontsource/merriweather/400.css" rel="stylesheet">
        <link href="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/@fontsource/merriweather/400-italic.css" rel="stylesheet">
            <link href="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/@fontsource/merriweather/700.css" rel="stylesheet">
        <link href="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/@fontsource/merriweather/700-italic.css" rel="stylesheet">
                <link href="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/@fontsource/ubuntu/300.css" rel="stylesheet">
        <link href="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/@fontsource/ubuntu/300-italic.css" rel="stylesheet">
            <link href="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/@fontsource/ubuntu/400.css" rel="stylesheet">
        <link href="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/@fontsource/ubuntu/400-italic.css" rel="stylesheet">
            <link href="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/@fontsource/ubuntu/500.css" rel="stylesheet">
        <link href="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/@fontsource/ubuntu/500-italic.css" rel="stylesheet">
            <link href="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/@fontsource/ubuntu/700.css" rel="stylesheet">
        <link href="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/@fontsource/ubuntu/700-italic.css" rel="stylesheet">
    
    <!-- DateRangePicker CSS -->
    <link href="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/bootstrap-daterangepicker/daterangepicker.css" rel="stylesheet">

    <!-- Editable and Select2 -->
    <link href="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/select2/dist/css/select2.css" rel="stylesheet">

    <link rel="shortcut icon" href="/favicon">

    <!-- Own CSS -->
    <link rel="stylesheet" href="/css/style.css?7bde9d=">
    <style type="text/css">           .logo {
         background-color: ;
     }
          :root {
                      --branding-border: linear-gradient(rgb(240,176,52), rgb(240,176,52));
              }

          div.page-content.clearfix.above-everything.alert.alert-danger { color: #31708f; background: #d9edf7; border-color: #bce8f1; }
div.page-content.clearfix.above-everything.alert.alert-danger div.main-content { padding-bottom: 0; }

         </style>

    <script type="text/javascript">
        window.page_loaded_at = new Date();
        jQuery.noConflict();
    </script><style></style>

    <script type="text/javascript">
    jQuery.ns = function (namespace) {
        var parts = namespace.split('.');
        var last = window;
        for (var i = 0; i < parts.length; i++) {
            last = last[parts[i]] || (last[parts[i]] = {});
        }
        return last;
    };
</script>
     <script>
const KattisErrorMessages = {"INTERNAL_SERVER_ERROR":"Internal server error.","ACCESS_DENIED":"Access denied.","NOT_AUTHENTICATED":"Not authenticated.","METHOD_NOT_ALLOWED":"Method not allowed.","INVALID_JSON":"JSON cannot be decoded or encoded data is deeper than the recursion limit.","BAD_CSRF_TOKEN":"Token does not match session's csrf_token","SESSION_NAME_EMPTY":"Session's name must be non empty.","SESSION_START_TIME_EMPTY":"Session's start time must be non empty.","SESSION_START_TIME_PASSED":"Session's start time has already passed.","SESSION_DURATION_EMPTY":"Session's duration must be non empty.","SESSION_DURATION_NEGATIVE":"Session's duration must be a positive number.","SESSION_DURATION_EXCEEDED":"Maximum duration for the session was exceeded.","SESSION_ALREADY_STARTED":"The session has already started.","SESSION_ALREADY_FINISHED":"The session is already finished.","USER_CREATED_SESSION_DURATION_EXCEEDED":"Contest cannot be longer than 168 hours.","INVALID_PROBLEM_SCORE":"Invalid problem score.","INVALID_PROBLEM_RGB":"Invalid problem color.","INVALID_SESSION_SHORTNAME":"Invalid shortname for the session.","INVALID_SESSION_CUTOFF":"Invalid cutoff for the session.","INVALID_USER_NAME":"Invalid username or email.","SESSION_NOT_FOUND":"No such session.","COURSE_NOT_FOUND":"No such course.","OFFERING_NOT_FOUND":"No such offering.","TEACHER_NOT_FOUND":"No such teacher.","TEACHER_CANNOT_REMOVE_SELF":"You may not remove yourself as a teacher unless you are an administrator.","AUTHOR_NOT_FOUND":"No such author.","JUDGE_NOT_FOUND":"No such judge.","JUDGE_ALREADY_EXIST":"The user is already a judge.","TEACHER_ALREADY_EXIST":"The user is already a teacher.","PROBLEM_NOT_FOUND":"No such problem.","TEAM_NOT_FOUND":"No such team.","SESSION_PROBLEM_ALREADY_EXIST":"The problem has been already added to the session.","SESSION_PROBLEM_DOES_NOT_EXIST":"The problem does not relate to the session.","PROBLEM_INDEX_NEGATIVE":"Problem index must be non negative.","AUTHOR_IS_CURRENT_TEAM_MEMBER":"The user you tried to add is already a member of the current team.","AUTHOR_IS_ANOTHER_TEAM_MEMBER":"The user you tried to add is already a member of another team in the current session.","AUTHOR_IS_JUDGE":"The user you tried to add is a judge.","AUTHOR_IS_NOT_TEAM_MEMBER":"The user you tried to remove is not a team member.","JUDGE_IS_TEAM_MEMBER":"The user you tried to add is a session team member or invitee.","SESSION_PUBLISHING_DENIED":"You do not have permission to publish this session.","CANNOT_PUBLISH_HISTORICAL_SESSION":"You cannot publish a session with a historical start time.","INVALID_TEAM_NAME_TOO_LONG":"The team name you are trying to add is too long","TEAM_NAME_IS_NOT_VISIBLE":"The team name you are trying to add is not visible","USER_COURSE_REGISTRATION_NEEDED":"You need to be registered to the course before you can join the assignment","INVITATION_NOT_FOUND":"Invitation could not be found"};
jQuery.extend(jQuery.ns('Kattis.error'), (function () {
    return {
        get_msg: function (error_code) {
            return KattisErrorMessages[error_code];
        },

        show_msg: function (base_message, error_code) {
            if (error_code) {
                alert(base_message + ": " + this.get_msg(error_code));
            } else {
                alert(base_message);
            }
        },

        show_xhr_msg: function (elem, jqXHR) {
            var base_message = elem.data('fail-msg');
            var code = jqXHR.responseJSON && jqXHR.responseJSON.error &&
                       jqXHR.responseJSON.error.code;
            this.show_msg(base_message, code);
        }
    }
})());
</script>
 
    
    <meta name="robots" content="noindex">
    <script src="/js/8cb58e4951798a7fc78fad722dc252f7/non-es6/mathjax_conf.js" defer=""></script>
<script src="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/tex-mml-chtml.js" defer="" id="MathJax-script"></script>
    <script defer="" src="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/ace-builds/src-min-noconflict/ace.js"></script>


    <script type="text/javascript">
var rumMOKey="a854f3a6dd7ee5e3b7d1641570b79c34";
(function(){
if(window.performance && window.performance.timing && window.performance.navigation) {
	var site24x7_rum_beacon=document.createElement('script');
	site24x7_rum_beacon.async=true;
	site24x7_rum_beacon.setAttribute('src','//static.site24x7rum.eu/beacon/site24x7rum-min.js?appKey='+rumMOKey);
	document.getElementsByTagName('head')[0].appendChild(site24x7_rum_beacon);
}
})(window)
</script><script async="" src="//static.site24x7rum.eu/beacon/site24x7rum-min.js?appKey=a854f3a6dd7ee5e3b7d1641570b79c34"></script>
<script src="https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/input/tex/extensions/noerrors.js" charset="UTF-8"></script><style type="text/css">.CtxtMenu_InfoClose {  top:.2em; right:.2em;}
.CtxtMenu_InfoContent {  overflow:auto; text-align:left; font-size:80%;  padding:.4em .6em; border:1px inset; margin:1em 0px;  max-height:20em; max-width:30em; background-color:#EEEEEE;  white-space:normal;}
.CtxtMenu_Info.CtxtMenu_MousePost {outline:none;}
.CtxtMenu_Info {  position:fixed; left:50%; width:auto; text-align:center;  border:3px outset; padding:1em 2em; background-color:#DDDDDD;  color:black;  cursor:default; font-family:message-box; font-size:120%;  font-style:normal; text-indent:0; text-transform:none;  line-height:normal; letter-spacing:normal; word-spacing:normal;  word-wrap:normal; white-space:nowrap; float:none; z-index:201;  border-radius: 15px;                     /* Opera 10.5 and IE9 */  -webkit-border-radius:15px;               /* Safari and Chrome */  -moz-border-radius:15px;                  /* Firefox */  -khtml-border-radius:15px;                /* Konqueror */  box-shadow:0px 10px 20px #808080;         /* Opera 10.5 and IE9 */  -webkit-box-shadow:0px 10px 20px #808080; /* Safari 3 & Chrome */  -moz-box-shadow:0px 10px 20px #808080;    /* Forefox 3.5 */  -khtml-box-shadow:0px 10px 20px #808080;  /* Konqueror */  filter:progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color="gray", Positive="true"); /* IE */}
</style><style type="text/css">.CtxtMenu_MenuClose {  position:absolute;  cursor:pointer;  display:inline-block;  border:2px solid #AAA;  border-radius:18px;  -webkit-border-radius: 18px;             /* Safari and Chrome */  -moz-border-radius: 18px;                /* Firefox */  -khtml-border-radius: 18px;              /* Konqueror */  font-family: "Courier New", Courier;  font-size:24px;  color:#F0F0F0}
.CtxtMenu_MenuClose span {  display:block; background-color:#AAA; border:1.5px solid;  border-radius:18px;  -webkit-border-radius: 18px;             /* Safari and Chrome */  -moz-border-radius: 18px;                /* Firefox */  -khtml-border-radius: 18px;              /* Konqueror */  line-height:0;  padding:8px 0 6px     /* may need to be browser-specific */}
.CtxtMenu_MenuClose:hover {  color:white!important;  border:2px solid #CCC!important}
.CtxtMenu_MenuClose:hover span {  background-color:#CCC!important}
.CtxtMenu_MenuClose:hover:focus {  outline:none}
</style><style type="text/css">.CtxtMenu_Menu {  position:absolute;  background-color:white;  color:black;  width:auto; padding:5px 0px;  border:1px solid #CCCCCC; margin:0; cursor:default;  font: menu; text-align:left; text-indent:0; text-transform:none;  line-height:normal; letter-spacing:normal; word-spacing:normal;  word-wrap:normal; white-space:nowrap; float:none; z-index:201;  border-radius: 5px;                     /* Opera 10.5 and IE9 */  -webkit-border-radius: 5px;             /* Safari and Chrome */  -moz-border-radius: 5px;                /* Firefox */  -khtml-border-radius: 5px;              /* Konqueror */  box-shadow:0px 10px 20px #808080;         /* Opera 10.5 and IE9 */  -webkit-box-shadow:0px 10px 20px #808080; /* Safari 3 & Chrome */  -moz-box-shadow:0px 10px 20px #808080;    /* Forefox 3.5 */  -khtml-box-shadow:0px 10px 20px #808080;  /* Konqueror */}
.CtxtMenu_MenuItem {  padding: 1px 2em;  background:transparent;}
.CtxtMenu_MenuArrow {  position:absolute; right:.5em; padding-top:.25em; color:#666666;  font-family: null; font-size: .75em}
.CtxtMenu_MenuActive .CtxtMenu_MenuArrow {color:white}
.CtxtMenu_MenuArrow.CtxtMenu_RTL {left:.5em; right:auto}
.CtxtMenu_MenuCheck {  position:absolute; left:.7em;  font-family: null}
.CtxtMenu_MenuCheck.CtxtMenu_RTL { right:.7em; left:auto }
.CtxtMenu_MenuRadioCheck {  position:absolute; left: .7em;}
.CtxtMenu_MenuRadioCheck.CtxtMenu_RTL {  right: .7em; left:auto}
.CtxtMenu_MenuInputBox {  padding-left: 1em; right:.5em; color:#666666;  font-family: null;}
.CtxtMenu_MenuInputBox.CtxtMenu_RTL {  left: .1em;}
.CtxtMenu_MenuComboBox {  left:.1em; padding-bottom:.5em;}
.CtxtMenu_MenuSlider {  left: .1em;}
.CtxtMenu_SliderValue {  position:absolute; right:.1em; padding-top:.25em; color:#333333;  font-size: .75em}
.CtxtMenu_SliderBar {  outline: none; background: #d3d3d3}
.CtxtMenu_MenuLabel {  padding: 1px 2em 3px 1.33em;  font-style:italic}
.CtxtMenu_MenuRule {  border-top: 1px solid #DDDDDD;  margin: 4px 3px;}
.CtxtMenu_MenuDisabled {  color:GrayText}
.CtxtMenu_MenuActive {  background-color: #606872;  color: white;}
.CtxtMenu_MenuDisabled:focus {  background-color: #E8E8E8}
.CtxtMenu_MenuLabel:focus {  background-color: #E8E8E8}
.CtxtMenu_ContextMenu:focus {  outline:none}
.CtxtMenu_ContextMenu .CtxtMenu_MenuItem:focus {  outline:none}
.CtxtMenu_SelectionMenu {  position:relative; float:left;  border-bottom: none; -webkit-box-shadow:none; -webkit-border-radius:0px; }
.CtxtMenu_SelectionItem {  padding-right: 1em;}
.CtxtMenu_Selection {  right: 40%; width:50%; }
.CtxtMenu_SelectionBox {  padding: 0em; max-height:20em; max-width: none;  background-color:#FFFFFF;}
.CtxtMenu_SelectionDivider {  clear: both; border-top: 2px solid #000000;}
.CtxtMenu_Menu .CtxtMenu_MenuClose {  top:-10px; left:-10px}
</style><style id="MJX-CHTML-styles">
mjx-container[jax="CHTML"] {
  line-height: 0;
}

mjx-container [space="1"] {
  margin-left: .111em;
}

mjx-container [space="2"] {
  margin-left: .167em;
}

mjx-container [space="3"] {
  margin-left: .222em;
}

mjx-container [space="4"] {
  margin-left: .278em;
}

mjx-container [space="5"] {
  margin-left: .333em;
}

mjx-container [rspace="1"] {
  margin-right: .111em;
}

mjx-container [rspace="2"] {
  margin-right: .167em;
}

mjx-container [rspace="3"] {
  margin-right: .222em;
}

mjx-container [rspace="4"] {
  margin-right: .278em;
}

mjx-container [rspace="5"] {
  margin-right: .333em;
}

mjx-container [size="s"] {
  font-size: 70.7%;
}

mjx-container [size="ss"] {
  font-size: 50%;
}

mjx-container [size="Tn"] {
  font-size: 60%;
}

mjx-container [size="sm"] {
  font-size: 85%;
}

mjx-container [size="lg"] {
  font-size: 120%;
}

mjx-container [size="Lg"] {
  font-size: 144%;
}

mjx-container [size="LG"] {
  font-size: 173%;
}

mjx-container [size="hg"] {
  font-size: 207%;
}

mjx-container [size="HG"] {
  font-size: 249%;
}

mjx-container [width="full"] {
  width: 100%;
}

mjx-box {
  display: inline-block;
}

mjx-block {
  display: block;
}

mjx-itable {
  display: inline-table;
}

mjx-row {
  display: table-row;
}

mjx-row > * {
  display: table-cell;
}

mjx-mtext {
  display: inline-block;
}

mjx-mstyle {
  display: inline-block;
}

mjx-merror {
  display: inline-block;
  color: red;
  background-color: yellow;
}

mjx-mphantom {
  visibility: hidden;
}

_::-webkit-full-page-media, _:future, :root mjx-container {
  will-change: opacity;
}

mjx-assistive-mml {
  position: absolute !important;
  top: 0px;
  left: 0px;
  clip: rect(1px, 1px, 1px, 1px);
  padding: 1px 0px 0px 0px !important;
  border: 0px !important;
  display: block !important;
  width: auto !important;
  overflow: hidden !important;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

mjx-assistive-mml[display="block"] {
  width: 100% !important;
}

mjx-math {
  display: inline-block;
  text-align: left;
  line-height: 0;
  text-indent: 0;
  font-style: normal;
  font-weight: normal;
  font-size: 100%;
  font-size-adjust: none;
  letter-spacing: normal;
  border-collapse: collapse;
  word-wrap: normal;
  word-spacing: normal;
  white-space: nowrap;
  direction: ltr;
  padding: 1px 0;
}

mjx-container[jax="CHTML"][display="true"] {
  display: block;
  text-align: center;
  margin: 1em 0;
}

mjx-container[jax="CHTML"][display="true"][width="full"] {
  display: flex;
}

mjx-container[jax="CHTML"][display="true"] mjx-math {
  padding: 0;
}

mjx-container[jax="CHTML"][justify="left"] {
  text-align: left;
}

mjx-container[jax="CHTML"][justify="right"] {
  text-align: right;
}

mjx-mi {
  display: inline-block;
  text-align: left;
}

mjx-c {
  display: inline-block;
}

mjx-utext {
  display: inline-block;
  padding: .75em 0 .2em 0;
}

mjx-mn {
  display: inline-block;
  text-align: left;
}

mjx-mo {
  display: inline-block;
  text-align: left;
}

mjx-stretchy-h {
  display: inline-table;
  width: 100%;
}

mjx-stretchy-h > * {
  display: table-cell;
  width: 0;
}

mjx-stretchy-h > * > mjx-c {
  display: inline-block;
  transform: scalex(1.0000001);
}

mjx-stretchy-h > * > mjx-c::before {
  display: inline-block;
  width: initial;
}

mjx-stretchy-h > mjx-ext {
  /* IE */ overflow: hidden;
  /* others */ overflow: clip visible;
  width: 100%;
}

mjx-stretchy-h > mjx-ext > mjx-c::before {
  transform: scalex(500);
}

mjx-stretchy-h > mjx-ext > mjx-c {
  width: 0;
}

mjx-stretchy-h > mjx-beg > mjx-c {
  margin-right: -.1em;
}

mjx-stretchy-h > mjx-end > mjx-c {
  margin-left: -.1em;
}

mjx-stretchy-v {
  display: inline-block;
}

mjx-stretchy-v > * {
  display: block;
}

mjx-stretchy-v > mjx-beg {
  height: 0;
}

mjx-stretchy-v > mjx-end > mjx-c {
  display: block;
}

mjx-stretchy-v > * > mjx-c {
  transform: scaley(1.0000001);
  transform-origin: left center;
  overflow: hidden;
}

mjx-stretchy-v > mjx-ext {
  display: block;
  height: 100%;
  box-sizing: border-box;
  border: 0px solid transparent;
  /* IE */ overflow: hidden;
  /* others */ overflow: visible clip;
}

mjx-stretchy-v > mjx-ext > mjx-c::before {
  width: initial;
  box-sizing: border-box;
}

mjx-stretchy-v > mjx-ext > mjx-c {
  transform: scaleY(500) translateY(.075em);
  overflow: visible;
}

mjx-mark {
  display: inline-block;
  height: 0px;
}

mjx-mspace {
  display: inline-block;
  text-align: left;
}

mjx-c::before {
  display: block;
  width: 0;
}

.MJX-TEX {
  font-family: MJXZERO, MJXTEX;
}

.TEX-B {
  font-family: MJXZERO, MJXTEX-B;
}

.TEX-I {
  font-family: MJXZERO, MJXTEX-I;
}

.TEX-MI {
  font-family: MJXZERO, MJXTEX-MI;
}

.TEX-BI {
  font-family: MJXZERO, MJXTEX-BI;
}

.TEX-S1 {
  font-family: MJXZERO, MJXTEX-S1;
}

.TEX-S2 {
  font-family: MJXZERO, MJXTEX-S2;
}

.TEX-S3 {
  font-family: MJXZERO, MJXTEX-S3;
}

.TEX-S4 {
  font-family: MJXZERO, MJXTEX-S4;
}

.TEX-A {
  font-family: MJXZERO, MJXTEX-A;
}

.TEX-C {
  font-family: MJXZERO, MJXTEX-C;
}

.TEX-CB {
  font-family: MJXZERO, MJXTEX-CB;
}

.TEX-FR {
  font-family: MJXZERO, MJXTEX-FR;
}

.TEX-FRB {
  font-family: MJXZERO, MJXTEX-FRB;
}

.TEX-SS {
  font-family: MJXZERO, MJXTEX-SS;
}

.TEX-SSB {
  font-family: MJXZERO, MJXTEX-SSB;
}

.TEX-SSI {
  font-family: MJXZERO, MJXTEX-SSI;
}

.TEX-SC {
  font-family: MJXZERO, MJXTEX-SC;
}

.TEX-T {
  font-family: MJXZERO, MJXTEX-T;
}

.TEX-V {
  font-family: MJXZERO, MJXTEX-V;
}

.TEX-VB {
  font-family: MJXZERO, MJXTEX-VB;
}

mjx-stretchy-v mjx-c, mjx-stretchy-h mjx-c {
  font-family: MJXZERO, MJXTEX-S1, MJXTEX-S4, MJXTEX, MJXTEX-A ! important;
}

@font-face /* 0 */ {
  font-family: MJXZERO;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Zero.woff") format("woff");
}

@font-face /* 1 */ {
  font-family: MJXTEX;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Main-Regular.woff") format("woff");
}

@font-face /* 2 */ {
  font-family: MJXTEX-B;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Main-Bold.woff") format("woff");
}

@font-face /* 3 */ {
  font-family: MJXTEX-I;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Math-Italic.woff") format("woff");
}

@font-face /* 4 */ {
  font-family: MJXTEX-MI;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Main-Italic.woff") format("woff");
}

@font-face /* 5 */ {
  font-family: MJXTEX-BI;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Math-BoldItalic.woff") format("woff");
}

@font-face /* 6 */ {
  font-family: MJXTEX-S1;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Size1-Regular.woff") format("woff");
}

@font-face /* 7 */ {
  font-family: MJXTEX-S2;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Size2-Regular.woff") format("woff");
}

@font-face /* 8 */ {
  font-family: MJXTEX-S3;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Size3-Regular.woff") format("woff");
}

@font-face /* 9 */ {
  font-family: MJXTEX-S4;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Size4-Regular.woff") format("woff");
}

@font-face /* 10 */ {
  font-family: MJXTEX-A;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_AMS-Regular.woff") format("woff");
}

@font-face /* 11 */ {
  font-family: MJXTEX-C;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Calligraphic-Regular.woff") format("woff");
}

@font-face /* 12 */ {
  font-family: MJXTEX-CB;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Calligraphic-Bold.woff") format("woff");
}

@font-face /* 13 */ {
  font-family: MJXTEX-FR;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Fraktur-Regular.woff") format("woff");
}

@font-face /* 14 */ {
  font-family: MJXTEX-FRB;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Fraktur-Bold.woff") format("woff");
}

@font-face /* 15 */ {
  font-family: MJXTEX-SS;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_SansSerif-Regular.woff") format("woff");
}

@font-face /* 16 */ {
  font-family: MJXTEX-SSB;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_SansSerif-Bold.woff") format("woff");
}

@font-face /* 17 */ {
  font-family: MJXTEX-SSI;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_SansSerif-Italic.woff") format("woff");
}

@font-face /* 18 */ {
  font-family: MJXTEX-SC;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Script-Regular.woff") format("woff");
}

@font-face /* 19 */ {
  font-family: MJXTEX-T;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Typewriter-Regular.woff") format("woff");
}

@font-face /* 20 */ {
  font-family: MJXTEX-V;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Vector-Regular.woff") format("woff");
}

@font-face /* 21 */ {
  font-family: MJXTEX-VB;
  src: url("https://open.kattis.com/assets/412bca7d79c8d6be9a7bed6d7a9919fd/mathjax/es5/output/chtml/fonts/woff-v2/MathJax_Vector-Bold.woff") format("woff");
}

mjx-c.mjx-c1D44E.TEX-I::before {
  padding: 0.441em 0.529em 0.01em 0;
  content: "a";
}

mjx-c.mjx-c1D44F.TEX-I::before {
  padding: 0.694em 0.429em 0.011em 0;
  content: "b";
}

mjx-c.mjx-c30::before {
  padding: 0.666em 0.5em 0.022em 0;
  content: "0";
}

mjx-c.mjx-c2264::before {
  padding: 0.636em 0.778em 0.138em 0;
  content: "\2264";
}

mjx-c.mjx-c2C::before {
  padding: 0.121em 0.278em 0.194em 0;
  content: ",";
}

mjx-c.mjx-c31::before {
  padding: 0.666em 0.5em 0 0;
  content: "1";
}

mjx-c.mjx-c2B::before {
  padding: 0.583em 0.778em 0.082em 0;
  content: "+";
}
</style><link id="freshworks-frame" rel="stylesheet" href="https://euc-widget.freshworks.com/widgetBase/static/media/frame.d7ae132c.css"></head>

<body class="">




<header class="l-page_header">
    <div class="page_header-arrow_expand_collapse">
        <i class="page_header-arrow_expand_collapse-arrow"></i>
    </div>
    <div class="page_header-wrapper">
        <div class="logo-container">
            <a class="logo-link" href="/" title="Kattis">
                <img class="logo" src="/images/site-logo?v=0a3f6018aacf449381741e45cf0ff6ba" alt="Kattis logo">
            </a>
            <h4 class="logo-container-text">Kattis</h4>
            <button class="menu_mobile_link">
                <i class="fas fa-bars menu_mobile_link_icon"></i>
            </button>
            <script type="module" src="/js/8cb58e4951798a7fc78fad722dc252f7/pages/master/nav.js"></script>
        </div>
        <div class="branding_border"></div>
        <div class="page_header-content">
            <nav>
                <ul class="main_menu">
                                                                    <li>
                            <a href="/problems" class="main_menu-item main_menu-item_link  is-main_menu-item-active" title="Problems">
                                                                    <i class="fas fa-brain main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name ">Problems</span>
                                                            </a>
                        </li>
                                                                    <li>
                            <a href="/contests" class="main_menu-item main_menu-item_link  " title="Contests">
                                                                    <i class="fas fa-award main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name ">Contests</span>
                                                            </a>
                        </li>
                                                                    <li>
                            <a href="/challenge" class="main_menu-item main_menu-item_link  " title="Challenge">
                                                                    <i class="fas fa-star main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name beta_label">Challenge</span>
                                                            </a>
                        </li>
                                                                    <li>
                            <a href="/ranklist" class="main_menu-item main_menu-item_link  " title="Ranklists">
                                                                    <i class="fas fa-trophy main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name ">Ranklists</span>
                                                            </a>
                        </li>
                                                                    <li>
                            <a href="/jobs" class="main_menu-item main_menu-item_link  " title="Jobs">
                                                                    <i class="fas fa-suitcase main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name ">Jobs</span>
                                                            </a>
                        </li>
                                                                    <li>
                            <a href="/help" class="main_menu-item main_menu-item_link  " title="Help">
                                                                    <i class="fas fa-question main_menu-item_icon"></i>
                                                                <span class="main_menu-item_name ">Help</span>
                                                            </a>
                        </li>
                                    </ul>
            </nav>
                            <div class="header_item_margin search-lower">
                    <label for="search_input" class="search-label search-label-right">Search</label>
                    <form id="search_form" method="GET" action="/search" class="search">
                                                    <img src="/images/site/header/logo-empty.png?0bb770=" alt="Kattis Cat" class="search-mascot">
                                                <input id="search_input" type="search" name="q" class="search-input" placeholder="Search Kattis">
                        <i id="search_submit" class="fas fa-search search-icon"></i>
                    </form>
                </div>
            
        </div>
    </div>
</header>

<script type="text/javascript">
    jQuery(function($) {
        $('.page_header-arrow_expand_collapse').click(function() {
            $('body').toggleClass('header-collapsed');
        });
    });
</script>



<main class="l-offset_main">
    

<div class="top_bar">
    <script type="module" src="/js/8cb58e4951798a7fc78fad722dc252f7/pages/master/top_bar.js"></script>
    <div class="branding_border"></div>
            <div class="top_bar-content-wrapper">
            <div class="top_bar-section top_bar-section-large">
                <div class="breadcrumb top_bar-item">
                                                                        <a href="/problems" class="breadcrumb-link">Problems</a><span class="breadcrumb-divider">/</span>
                                                                                    <span class="breadcrumb-current">
                                                    Add Two Numbers
                                            </span>
                </div>

                            </div>

            <div class="top_bar-section tooltip-right-container top_bar-section-small">

                
                                    <div class="top_bar-item top_bar-item-right top_bar-item-button top_bar-item-button-user">
                        <!-- Tooltip -->
                        <div class="tooltip-container">
                            <div class="top_bar-button" data-opentooltipid="top_user_tooltip" data-tooltiptype="right" data-tooltipusebackground="true">Saifur Rahman<i class="fas fa-chevron-down top_bar-button-chevron_down"></i><i class="fas fa-chevron-up top_bar-button-chevron_up"></i></div>
                            <div id="top_user_tooltip" class="tooltip" style="display: none;">
                                <span class="tooltip-arrow"></span>
                                <div class="tooltip-content tooltip-menu tooltip-top_bar">
                                    <i class="fas fa-times tooltip-close tooltip-top_bar-close"></i>
                                    <a href="/users/saifur-rahman2" class="image_info static_link"><div class="image_info-image-container"><object data="//:0" type="image/jpg" alt="Saifur Rahman" class="image_info-image image_info-image-strip image_info-image-rounded"><div class="image_info-image-overlay image_info-image-overlay-strip">SR</div><div class="image_info-image image_info-image-strip image_info-image-rounded image_info-image-icon"></div></object></div><div class="image_info-text-container"><span class="image_info-text-main image_info-text-main-user">Saifur Rahman</span><span class="image_info-text-sub"><ul class="image_info-list-sub"><li>Score: 2.4</li><li>Rank: 122338</li></ul></span></div></a>
                                    <ul class="main_menu profile_menu tooltip-top_bar-item">
                                                                                    <li>
                                                <a href="/users/saifur-rahman2/settings" class="main_menu-item main_menu-item_link profile_menu-item">
                                                    <i class="fas fa-user main_menu-item_icon"></i>Profile settings
                                                </a>
                                            </li>
                                                                                    <li>
                                                <a href="/users/saifur-rahman2" class="main_menu-item main_menu-item_link profile_menu-item">
                                                    <i class="fas fa-upload main_menu-item_icon"></i>My submissions
                                                </a>
                                            </li>
                                                                            </ul>
                                    <div class="tooltip-top_bar-item logout-container">
                                        <a href="/logout" class="button button-basic button-block">Log out<i class="fas fa-sign-out-alt button-icon-right"></i></a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                            </div>
        </div>
    </div>

    
    

<script type="module" src="/js/8cb58e4951798a7fc78fad722dc252f7/modules/mobile_tabs.js"></script>
<script type="module" src="/js/8cb58e4951798a7fc78fad722dc252f7/modules/load_select.js"></script>
<script type="module" src="/js/8cb58e4951798a7fc78fad722dc252f7/pages/problems/view.js"></script>
<script type="module">
    import initializeCopyButtons from "/js/8cb58e4951798a7fc78fad722dc252f7/modules/attach-copy-buttons.js";
    jQuery(document).ready(function($) {
        initializeCopyButtons("Copied to clipboard!");
    });
</script>

<div class="l-book">
    <div class="book-container">
        <div id="bookmark" class="book-bookmark is-hidden">
            <div class="book-bookmark-text" data-cy="instruction-bookmark">
                View problem statement: <span class="book-bookmark-text-subtext">Add Two Numbers</span><i class="fas fa-chevron-left book-bookmark-text-icon"></i>
            </div>
        </div>
		    <div id="instructions-container" class="book-page-container grow book-page-fixed_width">
            <article class="book-page">
                <div class="book-page-fixed_width">
					          <div id="instructions-close" class="book-close"><i class="fas fa-chevron-left book-close-icon"></i>Hide</div>
                    <h1 class="book-page-heading">Add Two Numbers</h1>
                                            
  <div class="problembody">
    <p>In this problem, your program should read two whole numbers
    (also called integers) from the input, and print out their
    sum.</p>
    <p>As a refresher, here are some ways to read two numbers from
    standard input in a few different languages:</p>
    <pre># Python 3
line = input()
a, b = line.split()
a = int(a)
b = int(b)

// C++
// make sure to first "#include &lt;iostream&gt;"
int a, b;
std::cin &gt;&gt; a &gt;&gt; b;

// Java
// make sure to first "import java.util.Scanner;"
Scanner s = new Scanner(System.in);
int a = s.nextInt(), b = s.nextInt();
</pre>
    <h2>Input</h2>
    <p>The input contains one line, which has two integers
    <span class="tex2jax_process"><mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" tabindex="0" ctxtmenu_counter="0" style="font-size: 125.6%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></mjx-assistive-mml></mjx-container></span> and <span class="tex2jax_process"><mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" tabindex="0" ctxtmenu_counter="1" style="font-size: 125.6%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math></mjx-assistive-mml></mjx-container></span>, separated by a single space. The
    bounds on these values are <span class="tex2jax_process"><mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" tabindex="0" ctxtmenu_counter="2" style="font-size: 125.6%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>≤</mo><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml></mjx-container></span>.</p>
    <h2>Output</h2>
    <p>Output the sum of the two integers, <span class="tex2jax_process"><mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" tabindex="0" ctxtmenu_counter="3" style="font-size: 125.6%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi></math></mjx-assistive-mml></mjx-container></span>.</p>
    <table class="sample" summary="sample data">
      <tbody><tr>
        <th>Sample Input 1</th>
        <th>Sample Output 1</th>
      </tr>
      <tr>
        <td>
          <pre>3 4
</pre>
        <span class="copy-to-clipboard"></span></td>
        <td>
          <pre>7
</pre>
        <span class="copy-to-clipboard"></span></td>
      </tr>
    </tbody></table>
    <table class="sample" summary="sample data">
      <tbody><tr>
        <th>Sample Input 2</th>
        <th>Sample Output 2</th>
      </tr>
      <tr>
        <td>
          <pre>987 23
</pre>
        <span class="copy-to-clipboard"></span></td>
        <td>
          <pre>1010
</pre>
        <span class="copy-to-clipboard"></span></td>
      </tr>
    </tbody></table>
  </div>

                                    </div>
            </article>
        </div>

        <div id="editor-container" class="book-page-container grow static-fixed-parent is-dragging-unnaffected" data-problem-name="addtwonumbers" data-submit-url="/problems/addtwonumbers/submit" data-sourcelim="131072" data-may-submit="true" data-csrf-token="5186750808275354224705279157743650534883">
            <div id="edit-and-submit-tab" class="tab static-fixed-content pb-4 " style="width: 593px; position: fixed; min-height: auto; margin-top: 0px; height: calc(100vh - (var(--main-padding-y) * 2) - 0px);">
                <div class="l-strip_list-flex no-overflow">
                    <div class="strip-plain">
                        <nav class="tab-nav" data-mobile-select-classes="is-hidden@md tab-select-js"><a id="edit-and-submit-tab-link" class="tab-nav-item tab-nav-js active" title="Edit &amp; Submit" data-tab-id-to-open="edit-and-submit-tab" data-tab-id-to-close="edit-and-submit-tab">Edit &amp; Submit</a><a id="metadata-tab-link" class="tab-nav-item tab-nav-js " title="Metadata" data-tab-id-to-open="metadata-tab" data-tab-id-to-close="edit-and-submit-tab">Metadata</a><a id="submissions-tab-link" class="tab-nav-item tab-nav-js " title="Submissions" data-tab-id-to-open="submissions-tab" data-tab-id-to-close="edit-and-submit-tab">Submissions</a><div class="tabs-close book-close-tabs">Hide <i class="fas fa-chevron-right book-close-icon"></i></div></nav><select class="is-hidden@md tab-select-js" data-default-value="edit-and-submit-tab/edit-and-submit-tab"><option value="edit-and-submit-tab/edit-and-submit-tab" selected="selected">Edit &amp; Submit</option><option value="metadata-tab/edit-and-submit-tab">Metadata</option><option value="submissions-tab/edit-and-submit-tab">Submissions</option></select>
                    </div>
                                            <div id="editor-container-editor" class="editor-container-content is-hidden">
                            <div class="editor-top">
                                <div class="editor-top-header_items">
                                    <div class="editor-top-pages editor-top-header_item">
                                        <template id="editor-file_template">
                                            <div class="editor-top-input">
                                                <div role="textbox" contenteditable="true" class="editor-top-input-field" data-pageid="-1"></div>
                                                <i class="fas fa-times editor-top-input-remove" contenteditable="false"></i>
                                            </div>
                                        </template>
                                    </div>

                                    <div class="editor-top-header-options editor-top-header_item">
                                        <div class="editor-top-header-option">
                                            <select id="editor_languages_list" name="editor_languages_list" class="select2 editor-select2 select2-hidden-accessible" data-select2-id="select2-data-editor_languages_list" tabindex="-1" aria-hidden="true">
                                                <option value="" data-select2-id="select2-data-2-cc71"></option>
                                                
            <option data-defaultextension="c" data-defaultcode="" data-defaultname="addtwonumbers" value="C">
            C
        </option>
            <option data-defaultextension="cs" data-defaultcode="" data-defaultname="addtwonumbers" value="C#">
            C#
        </option>
            <option data-defaultextension="cpp" data-defaultcode="" data-defaultname="addtwonumbers" value="C++">
            C++
        </option>
            <option data-defaultextension="cob" data-defaultcode="" data-defaultname="addtwonumbers" value="COBOL">
            COBOL
        </option>
            <option data-defaultextension="lisp" data-defaultcode="" data-defaultname="addtwonumbers" value="Common Lisp">
            Common Lisp
        </option>
            <option data-defaultextension="fs" data-defaultcode="" data-defaultname="addtwonumbers" value="F#">
            F#
        </option>
            <option data-defaultextension="f90" data-defaultcode="" data-defaultname="addtwonumbers" value="Fortran">
            Fortran
        </option>
            <option data-defaultextension="go" data-defaultcode="" data-defaultname="addtwonumbers" value="Go">
            Go
        </option>
            <option data-defaultextension="hs" data-defaultcode="" data-defaultname="addtwonumbers" value="Haskell">
            Haskell
        </option>
            <option data-defaultextension="java" data-defaultcode="" data-defaultname="addtwonumbers" value="Java">
            Java
        </option>
            <option data-defaultextension="js" data-defaultcode="" data-defaultname="addtwonumbers" value="JavaScript (Node.js)">
            JavaScript (Node.js)
        </option>
            <option data-defaultextension="js" data-defaultcode="" data-defaultname="addtwonumbers" value="JavaScript (SpiderMonkey)">
            JavaScript (SpiderMonkey)
        </option>
            <option data-defaultextension="kt" data-defaultcode="" data-defaultname="addtwonumbers" value="Kotlin">
            Kotlin
        </option>
            <option data-defaultextension="m" data-defaultcode="" data-defaultname="addtwonumbers" value="Objective-C">
            Objective-C
        </option>
            <option data-defaultextension="ml" data-defaultcode="" data-defaultname="addtwonumbers" value="OCaml">
            OCaml
        </option>
            <option data-defaultextension="pas" data-defaultcode="" data-defaultname="addtwonumbers" value="Pascal">
            Pascal
        </option>
            <option data-defaultextension="php" data-defaultcode="" data-defaultname="addtwonumbers" value="PHP">
            PHP
        </option>
            <option data-defaultextension="pl" data-defaultcode="" data-defaultname="addtwonumbers" value="Prolog">
            Prolog
        </option>
            <option data-defaultextension="py" data-defaultcode="" data-defaultname="addtwonumbers" value="Python 2">
            Python 2
        </option>
            <option data-defaultextension="py" data-defaultcode="" data-defaultname="addtwonumbers" value="Python 3">
            Python 3
        </option>
            <option data-defaultextension="rb" data-defaultcode="" data-defaultname="addtwonumbers" value="Ruby">
            Ruby
        </option>
            <option data-defaultextension="rs" data-defaultcode="" data-defaultname="addtwonumbers" value="Rust">
            Rust
        </option>
    
                                            </select><span class="select2 select2-container select2-container--default" dir="ltr" data-select2-id="select2-data-1-ijql" style="width: 100%;"><span class="selection"><span class="select2-selection select2-selection--single" role="combobox" aria-haspopup="true" aria-expanded="false" tabindex="0" aria-disabled="false" aria-labelledby="select2-editor_languages_list-container" aria-controls="select2-editor_languages_list-container"><span class="select2-selection__rendered" id="select2-editor_languages_list-container" role="textbox" aria-readonly="true"></span><span class="select2-selection__arrow" role="presentation"><b role="presentation"></b></span></span></span><span class="dropdown-wrapper" aria-hidden="true"></span></span>
                                        </div>
                                        <div class="editor-top-header-option">
                                            <button id="editor-add_page-button" class="editor-top-button">+ New</button>
                                        </div>
                                        <div class="editor-top-header-option">
                                            <i class="fas fa-upload editor-top-icon editor-top-upload"><input type="file" class="editor-top-upload-input" multiple=""></i>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div id="editor" class=" ace_editor ace_hidpi ace-tm"><div style="position: absolute;"></div><textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; font-size: 1px;"></textarea><div class="ace_gutter" aria-hidden="true"><div class="ace_layer ace_gutter-layer ace_folding-enabled" style="height: 1e+06px;"></div></div><div class="ace_scroller" style="line-height: 0px;"><div class="ace_content"><div class="ace_layer ace_print-margin-layer"><div class="ace_print-margin" style="left: 4px; visibility: visible;"></div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_text-layer" style="height: 1e+06px; margin: 0px 4px;"></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_cursor-layer ace_hidden-cursors"><div class="ace_cursor"></div></div></div></div><div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 20px;"><div class="ace_scrollbar-inner" style="width: 20px;">&nbsp;</div></div><div class="ace_scrollbar ace_scrollbar-h" style="display: none; height: 20px;"><div class="ace_scrollbar-inner" style="height: 20px;">&nbsp;</div></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;"><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;"></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div></div></div>
                            <div class="editor-bottom">
                                <div id="mainclass-container" class="mainclass-container-content">
                                    <label for="mainclass" class="mainclass-label">Mainclass:</label>
                                    <input type="text" id="mainclass" class="mainclass-field">
                                </div>
                                <button id="submit_code_button" class="button button-primary button-medium button-small ml-auto">Submit</button>
                            </div>
                            <div class="editor-drag_highlight is-hidden">
                                <i class="fas fa-upload editor-container-intro-icon"></i>
                                Upload file(s)                            </div>
                        </div>

                        <div id="editor-container-intro" class="editor-container-content">
                            <div class="editor-container-intro-content">
                                <div class="editor-container-intro-half">
                                    <div class="editor-container-intro-half-content">
                                        <i class="fas fa-code editor-container-intro-icon"></i>
                                        <p class="editor-container-intro-text">
                                            Select your programming language of choice and start writing your code.                                        </p>
                                        <div class="editor-container-intro-select">
                                            <select id="intro_language_select" name="intro_languages_list" class="select2 intro-select2 select2-hidden-accessible" data-placeholder="Choose language" data-select2-id="select2-data-intro_language_select" tabindex="-1" aria-hidden="true">
                                                <option value=""></option>
                                                
            <option data-defaultextension="c" data-defaultcode="" data-defaultname="addtwonumbers" value="C">
            C
        </option>
            <option data-defaultextension="cs" data-defaultcode="" data-defaultname="addtwonumbers" value="C#">
            C#
        </option>
            <option data-defaultextension="cpp" data-defaultcode="" data-defaultname="addtwonumbers" value="C++">
            C++
        </option>
            <option data-defaultextension="cob" data-defaultcode="" data-defaultname="addtwonumbers" value="COBOL">
            COBOL
        </option>
            <option data-defaultextension="lisp" data-defaultcode="" data-defaultname="addtwonumbers" value="Common Lisp">
            Common Lisp
        </option>
            <option data-defaultextension="fs" data-defaultcode="" data-defaultname="addtwonumbers" value="F#">
            F#
        </option>
            <option data-defaultextension="f90" data-defaultcode="" data-defaultname="addtwonumbers" value="Fortran">
            Fortran
        </option>
            <option data-defaultextension="go" data-defaultcode="" data-defaultname="addtwonumbers" value="Go">
            Go
        </option>
            <option data-defaultextension="hs" data-defaultcode="" data-defaultname="addtwonumbers" value="Haskell">
            Haskell
        </option>
            <option data-defaultextension="java" data-defaultcode="" data-defaultname="addtwonumbers" value="Java">
            Java
        </option>
            <option data-defaultextension="js" data-defaultcode="" data-defaultname="addtwonumbers" value="JavaScript (Node.js)">
            JavaScript (Node.js)
        </option>
            <option data-defaultextension="js" data-defaultcode="" data-defaultname="addtwonumbers" value="JavaScript (SpiderMonkey)">
            JavaScript (SpiderMonkey)
        </option>
            <option data-defaultextension="kt" data-defaultcode="" data-defaultname="addtwonumbers" value="Kotlin">
            Kotlin
        </option>
            <option data-defaultextension="m" data-defaultcode="" data-defaultname="addtwonumbers" value="Objective-C">
            Objective-C
        </option>
            <option data-defaultextension="ml" data-defaultcode="" data-defaultname="addtwonumbers" value="OCaml">
            OCaml
        </option>
            <option data-defaultextension="pas" data-defaultcode="" data-defaultname="addtwonumbers" value="Pascal">
            Pascal
        </option>
            <option data-defaultextension="php" data-defaultcode="" data-defaultname="addtwonumbers" value="PHP">
            PHP
        </option>
            <option data-defaultextension="pl" data-defaultcode="" data-defaultname="addtwonumbers" value="Prolog">
            Prolog
        </option>
            <option data-defaultextension="py" data-defaultcode="" data-defaultname="addtwonumbers" value="Python 2">
            Python 2
        </option>
            <option data-defaultextension="py" data-defaultcode="" data-defaultname="addtwonumbers" value="Python 3" selected="" data-select2-id="select2-data-4-ugpp">
            Python 3
        </option>
            <option data-defaultextension="rb" data-defaultcode="" data-defaultname="addtwonumbers" value="Ruby">
            Ruby
        </option>
            <option data-defaultextension="rs" data-defaultcode="" data-defaultname="addtwonumbers" value="Rust">
            Rust
        </option>
    
                                            </select><span class="select2 select2-container select2-container--default" dir="ltr" data-select2-id="select2-data-3-h5eu" style="width: 100%;"><span class="selection"><span class="select2-selection select2-selection--single" role="combobox" aria-haspopup="true" aria-expanded="false" tabindex="0" aria-disabled="false" aria-labelledby="select2-intro_language_select-container" aria-controls="select2-intro_language_select-container"><span class="select2-selection__rendered" id="select2-intro_language_select-container" role="textbox" aria-readonly="true" title="
            Python 3
        ">
            Python 3
        </span><span class="select2-selection__arrow" role="presentation"><b role="presentation"></b></span></span></span><span class="dropdown-wrapper" aria-hidden="true"></span></span>
                                        </div>
                                        <button id="start_coding_button" class="button button-primary button-medium editor-container-intro-button">Start coding</button>
                                    </div>
                                </div>

                                <div class="editor-container-intro-half editor-container-intro-drop">
                                    <div class="editor-container-intro-half-content">
                                        <i class="fas fa-upload editor-container-intro-icon"></i>
                                        <p class="editor-container-intro-text">
                                            You can also upload your files by drag &amp; drop here or by browsing your computer.                                        </p>
                                        <button id="upload_files_button" class="button button-primary button-medium upload_files_button editor-container-intro-button">
                                            <input type="file" class="upload_files_button-input" multiple="">
                                            Upload files...                                        </button>
                                    </div>
                                    <div class="editor-drag_highlight is-hidden">
                                    </div>
                                </div>
                            </div>
                        </div>
                                    </div>
		        </div>
            <div id="metadata-tab" class="tab static-fixed-content static-fixed-content-no-expand pb-4 is-hidden" data-bookmark-label="Metadata" style="width: 593px; position: fixed; min-height: auto; margin-top: 0px;">
                <div class="l-strip_list-flex no-overflow">
                    <div class="strip-plain">
                        <nav class="tab-nav" data-mobile-select-classes="is-hidden@md tab-select-js"><a id="edit-and-submit-tab-link" class="tab-nav-item tab-nav-js " title="Edit &amp; Submit" data-tab-id-to-open="edit-and-submit-tab" data-tab-id-to-close="metadata-tab">Edit &amp; Submit</a><a id="metadata-tab-link" class="tab-nav-item tab-nav-js active" title="Metadata" data-tab-id-to-open="metadata-tab" data-tab-id-to-close="metadata-tab">Metadata</a><a id="submissions-tab-link" class="tab-nav-item tab-nav-js " title="Submissions" data-tab-id-to-open="submissions-tab" data-tab-id-to-close="metadata-tab">Submissions</a><div class="tabs-close book-close-tabs">Hide <i class="fas fa-chevron-right book-close-icon"></i></div></nav><select class="is-hidden@md tab-select-js" data-default-value="metadata-tab/metadata-tab"><option value="edit-and-submit-tab/metadata-tab">Edit &amp; Submit</option><option value="metadata-tab/metadata-tab" selected="selected">Metadata</option><option value="submissions-tab/metadata-tab">Submissions</option></select>
                    </div>
                    <div class="book-page">
                        <div class="metadata_list">
                                                            
    <div class="metadata_list-item">
        <span class="metadata_list-label">CPU Time limit</span>
        <span>1 second</span>
    </div>

                                
    <div class="metadata_list-item">
        <span class="metadata_list-label">Memory limit</span>
        <span>1024 MB</span>
    </div>

                            
                                                                                                
                                                                        
    <div class="metadata_list-item">
        <span class="metadata_list-label">Difficulty</span>
        <span><span class="difficulty_number difficulty_number-problems_table difficulty_easy">1.4</span>Easy</span>
    </div>

                                                                                                                        
    <div class="metadata_list-item">
        <span class="metadata_list-label">Statistics</span>
        <span><a href="/problems/addtwonumbers/statistics">Show</a></span>
    </div>

                                                                                        
    <div class="metadata_list-item">
        <span class="metadata_list-label">My Submissions</span>
        <span><a href="/users/saifur-rahman2/submissions/addtwonumbers">Show</a></span>
    </div>

                                                                                        <div class="metadata_list-item">
                                    <span class="metadata_list-label">Downloads</span>
                                    <div class="metadata_list-downloads">
                                                                                    <a href="/problems/addtwonumbers/file/statement/samples.zip" download="addtwonumbers.zip" }="">
                                                Sample data files
                                            </a>
                                                                            </div>
                                </div>
                                                        
                                                            <div class="metadata_list-item">
                                    <span class="metadata_list-label">Author</span>
                                    <div>
                                        <a href="/problem-authors/Greg%20Hamerly">Greg Hamerly</a>                                    </div>
                                </div>
                            
                                                                                            
    <div class="metadata_list-item">
        <span class="metadata_list-label">Source</span>
        <span>                                                                            <a href="/problem-sources/Kattis">Kattis</a>
                                                                    </span>
    </div>

                            
                                                                                            
    <div class="metadata_list-item">
        <span class="metadata_list-label">License</span>
        <span>                                                                            <a rel="license" href="https://creativecommons.org/licenses/by-sa/3.0/" style="vertical-align: middle;">
                                                                                                                <img class="problem-license" alt="Creative Commons License (cc by-sa)" src="https://licensebuttons.net/l/by-sa/3.0/80x15.png">
                                                                                                                </a>
                                                                    </span>
    </div>

                                                    </div>
                    </div>
                </div>
            </div>
            <div id="submissions-tab" class="tab static-fixed-content  pb-4 is-hidden" data-bookmark-label="Submissions" style="width: 593px; position: fixed; min-height: auto; margin-top: 0px; height: calc(100vh - (var(--main-padding-y) * 2) - 0px);">
                <div class="l-strip_list-flex no-overflow">
                    <div class="strip-plain">
                        <nav class="tab-nav" data-mobile-select-classes="is-hidden@md tab-select-js"><a id="edit-and-submit-tab-link" class="tab-nav-item tab-nav-js " title="Edit &amp; Submit" data-tab-id-to-open="edit-and-submit-tab" data-tab-id-to-close="submissions-tab">Edit &amp; Submit</a><a id="metadata-tab-link" class="tab-nav-item tab-nav-js " title="Metadata" data-tab-id-to-open="metadata-tab" data-tab-id-to-close="submissions-tab">Metadata</a><a id="submissions-tab-link" class="tab-nav-item tab-nav-js active" title="Submissions" data-tab-id-to-open="submissions-tab" data-tab-id-to-close="submissions-tab">Submissions</a><div class="tabs-close book-close-tabs">Hide <i class="fas fa-chevron-right book-close-icon"></i></div></nav><select class="is-hidden@md tab-select-js" data-default-value="submissions-tab/submissions-tab"><option value="edit-and-submit-tab/submissions-tab">Edit &amp; Submit</option><option value="metadata-tab/submissions-tab">Metadata</option><option value="submissions-tab/submissions-tab" selected="selected">Submissions</option></select>
                    </div>
                                            <section class="strip table-wrapper scrollable-container">
                                                        


<table class="table2 report_grid-problems_table double-rows" id="submissions"><thead><tr><th> </th> <th>Judgement</th> <th>Runtime</th> <th>Language</th> <th>Test cases</th> <th> </th> </tr></thead><thead></thead><tbody><tr data-submission-id="10345399"><td data-type="plagiarism" style="min-width:0px"></td><td data-type="status" style="min-width:160px"><div class="status is-status-accepted"><i class="fas fa-check status-icon is-accepted"></i>Accepted</div></td><td data-type="cpu" style="min-width:80px">0.05&nbsp;s</td><td data-type="lang" style="min-width:110px">Python 3</td><td data-type="testcases" style="min-width:80px"><div class="horizontal_item">16/16</div></td><td data-type="actions" style="min-width:130px"><a href="/submissions/10345399" class="button button-basic button-tightsmall">View Details</a></td></tr><tr class="testcases-row"><td></td><td colspan="5"><div class="status testcase testcase-row"><i class="fas fa-check status-icon is-accepted" title="Test case 1/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 2/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 3/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 4/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 5/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 6/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 7/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 8/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 9/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 10/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 11/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 12/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 13/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 14/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 15/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 16/16: Accepted"></i></div></td></tr></tbody></table>                        </section>
                                    </div>
            </div>
			
        </div>
        <div id="bookmark-editor" class="book-bookmark is-hidden">
            <div class="book-bookmark-text" data-cy="editor-bookmark">
                Editor: <span id="editor-bookmark-label" class="book-bookmark-text-subtext" data-intro-text="Intro">Intro</span><i class="fas fa-chevron-right book-bookmark-text-icon"></i>
            </div>
        </div>
    </div>
</div>


    




    
    <script>
        window.fwSettings={
            'widget_id':79000000133
        };
        !function(){if("function"!=typeof window.FreshworksWidget){var n=function(){n.q.push(arguments)};n.q=[],window.FreshworksWidget=n}}()
    </script>
    <script type="text/javascript" src="https://euc-widget.freshworks.com/widgets/79000000133.js" async="" defer="" referrerpolicy="no-referrer"></script>
   

    <script>
        FreshworksWidget('identify', 'ticketForm', {
            name: 'Saifur Rahman',
                        email: 'msaifur92@gmail.com'
                    });
    </script>
</main>



<script src="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/moment/min/moment.min.js"></script>
<script src="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/bootstrap-daterangepicker/daterangepicker.js"></script>
<script src="/assets/412bca7d79c8d6be9a7bed6d7a9919fd/select2/dist/js/select2.full.min.js"></script>




<script defer="" src="https://static.cloudflareinsights.com/beacon.min.js/vaafb692b2aea4879b33c060e79fe94621666317369993" integrity="sha512-0ahDYl866UMhKuYcW078ScMalXqtFJggm7TmlUtp0UlD4eQk0Ixfnm5ykXKvGJNFjLMoortdseTfsRT8oCfgGA==" data-cf-beacon="{&quot;rayId&quot;:&quot;791acd211dd4d89d&quot;,&quot;token&quot;:&quot;6651308a007d4d459b12876077322bfb&quot;,&quot;version&quot;:&quot;2022.11.3&quot;,&quot;si&quot;:100}" crossorigin="anonymous"></script>


<div role="log" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"></div><div role="log" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"></div><div role="log" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"></div><div role="log" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"></div><div id="freshworks-container" data-html2canvas-ignore="true" style="width: 0px; height: 0px; bottom: 0px; right: 0px; z-index: 2147483647;"><div aria-live="polite"><iframe allowfullscreen="" id="launcher-frame" data-testid="launcher-frame" style="left: 22px; bottom: 22px; border: none; position: fixed; min-width: 104px; max-width: 156px; height: 56px; z-index: 2147483000; visibility: visible;"></iframe><iframe allowfullscreen="" id="lightbox-frame" data-testid="lightbox-frame" style="display: none;"></iframe></div></div><iframe title="FreshworksWidget" id="freshworks-frame" data-html2canvas-ignore="true" style="display: none;"></iframe></body></html>
