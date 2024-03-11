
// function AuthUser(url, title, width, height) {
//     let asc = OpenWin(url, title, width, height);
//     console.log(asc.closed)
// }

// function RegisterUser(url, title, width, height) {
//     OpenWin(url, title, width, height);
// }

// function OpenWin(url, title, width, height) {
//     let pos_left = window.screenLeft ? window.screenLeft : window.screenX;
//     let pos_top = window.screenTop ? window.screenTop : window.screenY;
//     console.log(`pos_left - ${pos_left}; pos_top - ${pos_top}`)
//     let left = pos_left + (window.innerWidth / 2) - (width / 2);
//     let top = pos_top + (window.innerHeight / 2) - (height / 2);
//     console.log(`left - ${left}; top - ${top}`)
    
//     return window.open(url, title, 'width=500, height=570, top=' + top + ', left=' + left);
// }

// function CloseWin (event) {
//     let btn = document.getElementById('confirmbtn');

//     console.log()
// }

// function winclose () {
//     close;
// }

function stopper () {
    alert("Извените данная опция в разработке")
}

function logOut () {
    // функция подтверждает выход пользователя из системы
    document.querySelector('form').onsubmit = function () {
        return confirm("Вы действительно хотите выйти?");
    }
}