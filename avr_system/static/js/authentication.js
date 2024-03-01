// AuthUser()

function AuthUser(url, title, width, height) {
    OpenWin(url, title, width, height);
}

function RegisterUser(url, title, width, height) {
    OpenWin(url, title, width, height);
}

function OpenWin(url, title, width, height) {
    let pos_left = window.screenLeft ? window.screenLeft : window.screenX;
    let pos_top = window.screenTop ? window.screenTop : window.screenY;
    console.log(`pos_left - ${pos_left}; pos_top - ${pos_top}`)
    let left = pos_left + (window.innerWidth / 2) - (width / 2);
    let top = pos_top + (window.innerHeight / 2) - (height / 2);
    console.log(`left - ${left}; top - ${top}`)

    return window.open(url, title, 'toolbar=no, location=no, directories=no, status=yes, menubar=no,scrollbars=yes, resizable=yes, copyhistory=no, width=500, height=570, top=' + top + ', left=' + left);
}

function CloseWin () {

    console.log('Работает консоль')
    if (window.opener.AuthUser()) {
        window.close();
    };
}
