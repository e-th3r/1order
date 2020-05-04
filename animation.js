let page = document.querySelector('.page');
let themeButton = document.querySelector('.theme-button');
themeButton.onclick = function()
{
	page.classList.toggle('yellow-bgtheme');
	page.classList.toggle('green-bgtheme')
};