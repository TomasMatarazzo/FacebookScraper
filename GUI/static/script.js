// Object that creates de Dropdown bar

function Dropdown(object){

    this.options = object;

    window.getparent = function(element){
        var id = element.closest('.dropdown').parentElement.id;
        console.log(window.dropdowns[id])
        return window.dropdowns[id];
    }

    this.init = function(){
        // Searching the id

        this.element = document.getElementById(this.options.id);

        //Creating the base html

        var value = this.options.val;
        var phrase = this.options.phrase;
        var html = '<h2>' + phrase + '</h2>'+'<div class = "dropdown"><div class = "dropdown_value" id = "NULL">'+ value + '</div>'
                        + '<div class = "dropdown_arrow"> ↧</div><div class = "dropdown_panel"><div class = "dropdown_items"></div></div>';
        this.element.innerHTML = html;

        // Store a hash of dropdowns

        if (!window.dropdowns) window.dropdowns ={};
        window.dropdowns[this.options.id] = this;

        // Get elements

        this.panel = this.element.querySelector('.dropdown_panel');
        this.items = this.element.querySelector('.dropdown_items');
        this.arrow = this.element.querySelector('.dropdown_arrow');
        this.value = this.element.querySelector('.dropdown_value');

        //Populate dropdown items
        var data = this.options.data;
        var html = "";
        data.forEach((element,i) => {
            html += '<div class = "dropdown_item" id = '+ i +' onmousedown =  "var self = getparent(this); self.clicked(this)"> '+ element +' </div>'
        });
        console.log(html);
        this.items.innerHTML = html;

        //Events
        var self = this;
        this.element.addEventListener('mousedown', ()=>{
                    if (self.isVisible)
                        self.hide();
                    else
                        self.show();
        });
    }

    this.init();

    this.clicked = function(element){
        event.stopPropagation();
        this.hide();

        var newval = element.innerHTML;
        this.value.innerHTML = newval;
        this.value.id = element.id;
    }
    this.show = function(){
        this.isVisible = true;
        this.items.style.transform = 'translate(0,0%)';
        this.arrow.style.transform = 'rotate(180deg)';
        this.panel.style.height = '400%' ;
    }

    this.hide = function(){
        this.isVisible = false;
        this.items.style.transform = 'translate(0,-100%)';
        this.arrow.style.transform = 'rotate(0deg)';
        this.panel.style.height = '100%' ;
    }

    return this;
}


var menu = new Dropdown({
    id: "dd1",
    phrase: "Choose value",
    val:"Location",
    data:['Alberta','Vancouver','Winnipeg','Ontario','Quebec','jacksonville']
});

var menu2 = new Dropdown({
    id: "dd2",
    phrase: "Type of advertisement",
    val:"-",
    data:['Home Sale','House Rental']
});


var menu3 = new Dropdown({
    id: "dd3",
    phrase: "Filters",
    val:"-",
    data:['--','--']
});

console.log("hi");