const Agent = require('../core/Agent');

/**
 * Simple reflex agent. Search for an object whithin a labyrinth. 
 * If the object is found the agen take it.
 */
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
        this.state = initialState
    }

    /**
     * Actuliza la posicion del raton en el entorno del raton y en el estado 
     * @param {x: integer, y: integer} position 
     */
    updatex(position){

        this.entorno[this.state.y][this.state.x]=1
        this.state.x=position.x
        this.state.y=position.y
        // console.log(this.entorno)

    }

    /**
     * Esta funcion  actualiza el entorno
     * y retorna la accion que el raton va a tomar y la posicion de esa accion (util para actualizar el modelo de entorno)
     * @returns 
     */
    setAction(){
        let viewKey = this.perception.join();
        let possibleActions= this.table[viewKey];
        this.updateEntorno()
        if(!possibleActions){
            possibleActions = this.table['default']
        }

        for(let i=0; i<possibleActions.length;i++){
            let x=this.state.x
            let y=this.state.y
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
            //console.log(this.perception)
            if(this.entorno[y][x] !== 1){
                // console.log(possibleActions[i])
                return [possibleActions[i],{x:x,y:y}]
            }

        }
        
        
    }

    /**
     * We override the send method. 
     * In this case, the state is just obtained as the join of the perceptions
     */
    send() {
        let [action,position] = this.setAction()
      
        this.updatex(position)
        //this.showMatrix(this.entorno)

        return action;

    }

    /**
     * Funcion auxiliar que muestra la matriz, sirve para visualizar el modelo de entorno del raton
     */
    showMatrix(matrix){
        let m= JSON.parse(JSON.stringify(matrix))
        m[this.state.y][this.state.x]='x'
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
    //    console.log(this.perception)
        this.createColumn(this.state.y)
        // this.entorno[this.state.y][this.state.x]=0
        let x=this.state.x
        let y= this.state.y
        //LEFT
        if(x-1>=0){
            if(this.entorno[this.state.y][this.state.x-1] !== 1){
            this.entorno[this.state.y][this.state.x-1]=this.perception[0]
            }
        }
        //UP
        if(y-1>=0){
            
            this.createColumn(this.state.y-1)
            if(this.entorno[this.state.y-1][this.state.x] !== 1){
            this.entorno[this.state.y-1][this.state.x]=this.perception[1]
            }
        }
        //RIGHT
        if(this.entorno[this.state.y][this.state.x+1] !== 1){
        this.entorno[this.state.y][this.state.x+1]=this.perception[2]
        }
        //DOWN
        this.createColumn(this.state.y+1)
        if(this.entorno[this.state.y+1][this.state.x] !== 1){
        this.entorno[this.state.y+1][this.state.x]=this.perception[3]
        }
    } 

}



module.exports = CleanerAgent;