
type ID = string |number ; 
export class Task<T = string >
{
    public taskName:string ; 
    public id:ID;
    public content:Array<T>|null = null;
    length=0 ;
    constructor (taskName:string,id:ID,...content:T[])
    {
        this.taskName = taskName ; 
        this.id = id;
        if (content !==null && content.length >0)
        {
            this.content = content; 
            this.length = content.length ; 
        }
        
    }
    do()
    { 
        if(this.content === null)return ; 

        for (const value of this.content )
        {
            console.log(value); 
        }
    }
} ; 

