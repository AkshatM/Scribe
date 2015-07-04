function update_window_list{
    var compose_ids = Array.prototype.slice.call(document.getElementsByClassName("Am Al editable LW-avf va_ar"));//for compose windows
    var reply_ids = Array.prototype.slice.call(document.getElementsByClassName("Am a09 Al editable LW-avf va_ar"));//for reply windows
    var windows = compose_ids.concat(reply_ids);
    return windows
}

var windows = setInterval(update_window_list, 3000);


