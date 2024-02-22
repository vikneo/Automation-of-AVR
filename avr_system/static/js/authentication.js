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

const CloseWin = () => { // объявляем функцию закрытия модального окна
    const modals = document.querySelectorAll('.modal') // ищем все модальные окна
    if (!modals) return // если их нет, то прекращаем выполнение функции
    modals.forEach(el => { // если есть, то для каждого из них
        el.addEventListener('click', e => { // при клике
            if (e.target.closest('.modal__close')) { // если клик был клик на кнопке закрытия
                el.classList.remove('modal_active') // то скрываем модальное окно, удаляя активный класс
            }
            if (!e.target.closest('.modal__body')) { // если клик был за пределами контентной части модального окна, то есть на затемненную область
                el.classList.remove('modal_active') // то тоже скрываем модальное окно, удаляя активный класс
            }
        })
    })
}