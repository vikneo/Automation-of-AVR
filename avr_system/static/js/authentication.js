
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
    alert("Извените! Данная опция в разработке")
}

function logOut () {
    // функция подтверждает выход пользователя из системы
    document.querySelector('form').onsubmit = function () {
        return confirm("Вы действительно хотите выйти?");
    }
}

function searchField () {

    let elem = document.getElementById('search')[0].value

    btn_search.onclick = function(event) {
        if (event.which == 1) {
            form.onsubmit = function () { return true;}
        }
    }
    
    if (elem.length < 2 ) {
        console.log(`Не достаточно символов для поиска`);
        form.onsubmit = function () { return false;}
        }
}

function mobileWin () {
    console.log(screen.width)
    if (screen.width < 560) {
        document.getElementById('screen').innerHTML = `<div style="display: none"></div>`;
        document.getElementById('advantage').innerHTML = `<div style="display: none"></div>`;
    }
}