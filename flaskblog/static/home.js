function Choice(){
    var navbartheme=document.getElementById("navbar-theme");
    var theme=document.getElementById("theme");
    var block=document.getElementById("block");
    var write=document.getElementById("write");
    var mydiv=document.getElementById("mydiv");

    if(block.getAttribute('class')=="buttom"){
        navbartheme.setAttribute('class',"navbar navbar-expand-sm navbar-dark bg-warning");
        theme.setAttribute('class',"bg-dark");
        theme.transitionDuration="1s";
        block.setAttribute('class','onit');
        block.transitionDuration="1s";
        write.innerHTML="Light Theme";
        write.transitionDuration="1s";
        mydiv.setAttribute('class',"container-fluid p-3 my-3 bg-warning text-black");



    }
    else if(block.getAttribute('class')=="onit"){
        navbartheme.setAttribute('class',"navbar navbar-expand-sm navbar-dark bg-primary");
        theme.setAttribute('class',"bg-light");
        block.setAttribute('class','buttom');
        mydiv.setAttribute('class',"container-fluid p-3 my-3 bg-primary text-black");
        block.transitionDuration="1s";
        write.innerHTML="Dark Theme";
        write.transitionDuration="1s";
        mydiv.setAttribute('class',"container-fluid p-3 my-3 bg-primary text-white");


    }

    
}