function Game() {
    this.stage = new Kinetic.Stage({
        container: 'game',
        width: document.getElementById("game").clientWidth,
        height: window.innerHeight * 0.80
    });
    this.cards = new Kinetic.Layer();
    this.startx = 5;

    common_props = {}
    common_props.width = 50;
    common_props.height = 2 * common_props.width;
    common_props.x = this.startx;
    common_props.y = this.stage.getHeight() - common_props.height - 5;
    
    this.rect_props = {
        fill: 'white', cornerRadius: 5,
        stroke: 'black', strokeWidth: 1,
        shadowColor: 'black', shadowBlur: 2, 
        shadowOffset: [2, 2], shadowOpacity: 0.2
    }
    this.text_props = {
        fontSize: 12, padding: 5, fill: 'black', align: 'center',
        text: "" 
    }
    for(key in common_props){
        this.rect_props[key] = common_props[key];
        this.text_props[key] = common_props[key];
    }
}

Game.prototype = {
    _create: function (card){
        this.rect_props.x = this.startx;
        this.text_props.x = this.startx;
        this.text_props.text = card.value + "\n" + card.color + "\n" +
                               card.name;
        
        var group = new Kinetic.Group({draggable: true});
        var rect = new Kinetic.Rect(this.rect_props);
        var text = new Kinetic.Text(this.text_props);

        group.add(rect);
        group.add(text);
        group.on('mouseover', function() {
            document.body.style.cursor = 'pointer';
        });
        group.on('mouseout', function() {
            document.body.style.cursor = 'default';
        });

        // increase x position
        this.startx = this.startx + 55;

        this.cards.add(group);
    },

    create: function(cards){
        for(var i = 0; i < cards.length; i++)
            this._create(cards[i]);
    },

    display: function(){
        this.stage.add(this.cards); 
    }
}
