const DropMenuButton = document.querySelector(".menu-icon");
const DropMenuWrapper = document.querySelector(".drop-menu");
let i = 1;
DropMenuButton.onclick = function(){
	if (i % 2){
		DropMenuWrapper.style.display = 'inline';
		
	}else{
		DropMenuWrapper.style.display = 'none';
	}
	i++;
}