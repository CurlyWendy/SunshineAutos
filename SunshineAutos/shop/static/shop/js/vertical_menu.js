
        // Получаем все заголовки h5 в меню
var h5Elements = document.querySelectorAll('.vertical-menu h5');

        // Добавляем обработчик события на каждый заголовок
h5Elements.forEach(function (h5) {
    h5.addEventListener('click', function () {
                // Находим все элементы li, содержащие подменю .sub-menu
        var parentLi = h5.closest('li');
        var subMenus = parentLi.querySelectorAll('.sub-menu');

                // Перебираем все подменю и изменяем их видимость
        subMenus.forEach(function (subMenu) {
            if (window.getComputedStyle(subMenu).getPropertyValue('display') === 'block') {
                subMenu.style.display = 'none';
            } else {
                subMenu.style.display = 'block';
            }
        });
    });
});