const Agent = require('../core/Agent');


class CleanerAgent extends Agent {
    constructor(value) {
        super(value);
        //LEFT, UP, RIGHT, DOWN, CELL
        this.table = {
            "0,0,0,0,0": ["LEFT", "UP", "RIGHT", "DOWN"],
            "0,0,0,1,0": ["LEFT", "UP", "RIGHT"],
            "0,0,1,0,0": ["LEFT", "UP", "DOWN"],
            "0,0,1,1,0": ["LEFT", "UP"],
            "0,1,0,0,0": ["LEFT", "RIGHT", "DOWN"],
            "0,1,0,1,0": ["LEFT", "RIGHT"],
            "0,1,1,0,0": ["LEFT", "DOWN"],
            "0,1,1,1,0": ["LEFT"],
            "1,0,0,0,0": ["UP", "RIGHT", "DOWN"],
            "1,0,0,1,0": ["UP","RIGHT"],
            "1,0,1,0,0": [ "UP", "DOWN"],
            "1,0,1,1,0": ["UP"],
            "1,1,0,0,0": ["RIGHT", "DOWN"],
            "1,1,0,1,0": ["RIGHT"],
            "1,1,1,0,0": ["DOWN"],
            "default": ["TAKE"]
        };
        this.entorno=[[]]
    }
    
    setup(initialState = {}) {
        this.initialState = initialState
        this.state=initialState
    }
    updatex(position){
         //sumar a la celda que se visitó
        this.entorno[this.state.raton.y][this.state.raton.x]+=1
        this.state.raton.x=position.x
        this.state.raton.y=position.y

    }
    //Funcion para decidir que accion se va a tomar con la percepcion obtenida
    setAction(){
        //obtener la percepcion sin la posicion 
        let viewKey = this.perception.slice(0,5).join();
        let possibleActions= this.table[viewKey];
        this.updateEntorno()
        if(!possibleActions){
            //si no hay mas acciones entonces se come
            possibleActions = this.table['default']
        }
        //objeto definido para determinar la celda a la que hay que ir
        let menor={
            distance:Number.POSITIVE_INFINITY,//Distancia en L de esta celda al queso
            value: 0, //cantidad de veces que ha sido visitada la celda en la posicion x y
            x:0,
            y:0,
            action:""
        }
        for(let i=0; i<possibleActions.length;i++){
            let x=this.state.raton.x
            let y=this.state.raton.y
            switch (possibleActions[i]){
                case 'UP':
                    y-=1
                    break
                case 'DOWN':
                    y+=1
                    break
                case 'RIGHT':
                    x+=1
                    break
                case 'LEFT':
                    x-=1
                    break   
        
            }
            if(x<0)x=0
            
            if(y<0)y=0
            //Sacar la distancia en L entre la celda que se esta considerando y el queso
            let chebyDist=Math.max(Math.abs(this.state.queso.x-x),Math.abs(this.state.queso.y-y))
            //revisar si la nueva posible accion va a una celda que ha sido visitada menos cantidad de veces
            //y esta mas cerca del queso
            if(menor.distance >= chebyDist  && menor.value >= this.entorno[y][x]){
                
                menor.distance=chebyDist
                menor.x=x
                menor.y=y
                menor.action=possibleActions[i]
                
            }
        }
            
            
                
            return [menor.action,{x:menor.x,y:menor.y}]

    }

    /**
     * We override the send method. 
     */
    send() {
        
        let [action,position] = this.setAction()
      
        this.updatex(position)

        return action;

    }
    /**
     * Funcion auxiliar que muestra la matriz, sirve para visualizar el modelo de entorno del raton
     */
    showMatrix(matrix){
        let m= JSON.parse(JSON.stringify(matrix))
        m[this.state.raton.y][this.state.raton.x]='x'
        for (let line of m) {
            console.log(line)
        }
    }
    /**
     * Crea una columna en caso de no existir, esto permite crear de forma dinamica una matriz nxm que es la estructura de datos 
     * @param {integer} y 
     */
    createColumn(y){
        if(!this.entorno[y]){
            this.entorno[y]=[]
        }
    }
     /**
     * Actualiza el entorno del raton de acuerdo a la percepcion que recibe
     */
    updateEntorno(){
        //LEFT, UP, RIGHT, DOWN, CELL
        this.createColumn(this.state.raton.y)
        let x=this.state.raton.x
        let y= this.state.raton.y
        //LEFT
        if(x-1>=0){
            if(this.entorno[this.state.raton.y][this.state.raton.x-1] !== 1){
            this.entorno[this.state.raton.y][this.state.raton.x-1]=this.perception[0]
            }
        }
        //UP
        if(y-1>=0){
            
            this.createColumn(this.state.raton.y-1)
            if(this.entorno[this.state.raton.y-1][this.state.raton.x] !== 1){
            this.entorno[this.state.raton.y-1][this.state.raton.x]=this.perception[1]
            }
        }
        //RIGHT
        if(this.entorno[this.state.raton.y][this.state.raton.x+1] !== 1){
        this.entorno[this.state.raton.y][this.state.raton.x+1]=this.perception[2]
        }
        //DOWN
        this.createColumn(this.state.raton.y+1)
        if(this.entorno[this.state.raton.y+1][this.state.raton.x] !== 1){
        this.entorno[this.state.raton.y+1][this.state.raton.x]=this.perception[3]
        }

        
    
    }

}


module.exports = CleanerAgent;