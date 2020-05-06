let page = document.querySelector('.page');
let themeButton = document.querySelector('.btn-7');
themeButton.onclick = function()
{
	page.classList.toggle('yellow-bgtheme');
	page.classList.toggle('green-bgtheme')
};