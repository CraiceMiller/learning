interface StackProps<V> {
    /**Only retive the current size of the stack */
    size():number; 
    /**
     *@param value the item to be pushed onto the stack
    * @Returns:the item arguemnt */
    push(value:V):boolean ; 
    /**
     * @returns
    the object at the top of this stack(The last item of the object)
    *@throws ValueError if this stack is empty
     */
    peek():V;
    /**
     * @description remove the top object of this stack Return:
    the object at the top of this stack(The last item of the object)
    *@throws ValueError if this stack is empty
     * @returns 
     */
    pop():V ; 
    /**
     * @returns boolean, meaning if the stack is empty or not
     */
    empty():boolean ; 
    /**
     * 
     * @description Return the 1-based position where an object is on this stack. if the param 'obj' occurs as an item in this stack, this method return the distance from the top of the stack of the occurence nearest the top of the stack; the topmost item on the stack is considered to be at distance. Parameters:
    * @param obj: the desired object
    *@returns the 1-based position from the top of the stack where the object is located.
     */
    search(obj:V):number ; 
}



export class Stack<T = string> implements StackProps<T>{
    public DATA:T[] = []; 
    constructor(){
        this.DATA = [] ; 
    }
    size():number{
        return this.DATA.length ; 
    }
    peek():T{
        let value:T | undefined = this.DATA[this.size() -1] ; 
        if (value === undefined){
            throw new Error("The Stack is empty") 
        }
        return value ; 
    }

    pop():T{
        let value:T|undefined  = this.DATA.pop(); 
        if(this.empty()|| value === undefined ){
            throw new Error("The Stack is currently empty"); 
        }

        return value 
    }
    push(value:T){
        this.DATA.push(value);
        return true ; 
    }
    empty():boolean{
        return this.DATA.length <= 0 ; 
    }

    search(obj: T): number {
        if (this.empty()){
            return -1 ; 
        }
        let index = this.DATA.indexOf(obj) ; 
        return index === -1 ? -1:this.size() - index ; 
    }

    get data(){
        return this.DATA ; 
    }
    
}
/**
 * @description An abstract base class representing a collection designed for holding
    elements prior to processing. Besides the methods inherited from
    Collection, this interface provides methods for adding, removing,
    and inspecting elements.

    The methods come in two forms: one throws an exception if the operation
    fails, the other returns a special value (None or False).
 */
export interface Queue<T>{
    /**
     * @description Inserts the specified element into this queue.
        
    *@param The element to add.
        
    @throw Exception: If the element cannot be added due to capacity
                       restrictions or other implementation-specific issues.
     */
    add(element:T): void; 
    /**
     * @description """
        Inserts the specified element into this queue if possible.
        
        *@param element: The element to add.
            
        @returns:
            True if the element was added, False otherwise.
        """
     */
    offer(element:T):boolean ; 
    /**
     * @description """
        Retrieves and removes the head of this queue.
        
        *@returns:
            The head of this queue.
            
        *@throws Error : If this queue is empty.
        """
     * 
     */
    remove():T; 
    /**
     * @descripton Retrieves and removes the head of this queue, or returns None
        if this queue is empty.
        
        *@returns:
            The head of this queue, or None if the queue is empty.
     */
    poll():T|null; 
    /**
     * @descripton Retrieves, but does not remove, the head of this queue.
        
        *@returns :
            The head of this queue.
            
        *@throws:
            IndexError: If this queue is empty.
     */
    element():T; 
    /**
     * @descrioption  Retrieves, but does not remove, the head of this queue, or
        returns None if this queue is empty.
        
        *@returns   The head of this queue, or None if the queue is empty.
     */
    peek():T|null ;
    /**
     *@description verify if the queue is empty
     */
    empty():boolean ; 
}

class Node<V> {
    public data: V   ; 
    public prev: Node<V> | null = null ; 
    public next:Node<V> | null = null ; 
    constructor(data:V,previous:Node<V>  | null = null ,next: null | Node<V>  = null){
        this.data = data; 
        this.prev = previous ; 
        this.next = next ; 
    }
}
/**
 * @desription """_summary_
        A linked list is a linear data structure that stores a collection of data elements
        in a sequence. Unlike an array, a linked list does not store its elements in contiguous
        memory locations. Instead, it consists of individual objects called nodes, where each node
        contains the data itself and a reference (or link) to the next node in the sequence
    
    Core components
        Node: The fundamental building block of a linked list. It contains two parts: the data and a pointer to the next node.
        Head: A reference to the first node in the list. This is the starting point for all operations.
        Tail: A reference to the last node in the list. In a standard linked list, this node's next pointer is None (or null).
        
        
    Types of linked lists
        Singly-linked list: Each node points only to the next node in the sequence. Traversal is possible in only one direction.
        Doubly-linked list: Each node has two references: one to the next node and one to the previous node.
        This allows for traversal in both forward and backward directions.
        Circular linked list: The last node points back to the first node, forming a loop. 


    How it works
        The LinkedList class manages the overall structure by keeping track of the head and tail nodes.
        Operations like adding or removing elements involve changing the pointers of the nodes, which
        can be done without reallocating or shifting the entire structure. 
        
    Advantages and disadvantages
        Advantages
           - Dynamic size: Can easily grow or shrink at runtime without the need for fixed-size memory allocation;
           - Efficient modifications: Inserting or deleting elements is fast and easy, especially at the beginning of the list.
            
        Disadvantages
                - Slower access: Retrieving an element by its position is inefficient, requiring a linear scan; 
                -  Higher memory usage: The extra space needed for pointers results in a higher memory footprint compared to arrays. 

    Args:
        QueueInterface (_type_): _description_
            This is the same to do this in typeScript:
                myList = LinkList<number>([1,2,3,4])
                
    *@example 
        >>> my_list:LinkList[int] = LinkList([1,2,3,4])
        >>> a:bool= my_list.offer(5)
        >>> b:int = my_list.remove()
                
    """
   
 */
export class LinkedList<T> implements Queue<T> {
    private head : Node<T> | null = null ; 
    private tail : Node<T> | null = null ; 
    private Size: number  =  0 ; 

    constructor(data?:T[]){
        this.head = null ; 
        this.tail = null ; 
        this.Size = 0 ; 

        if (data){
            this.extends(data) ; 
        }

        
    }

    //helpers 
    private addElementAtLast(info:T){
        const lastElement = this.tail ; 
        const newData:Node<T> = new Node(info,lastElement,null) ; 
        this.tail = newData ; 

        if (lastElement=== null) {
            this.head = newData ;
        }else{
            lastElement.next = newData ; 
        }

        this.Size ++ ; 
    }

    private removeElementAtFirst():T{
        if (this.head === null){
            throw new Error("The queue is empty") ; 
        }


        const firstElement = this.head ; 
        const lastData = this.head.data ; 

        this.head = firstElement.next ; 

        if (this.head === null){
            this.tail = null ; 
        }else{
            this.head.prev = null ; 
        }
        this.Size -- ; 

        return lastData ; 
    }

    //main properties to use 
    add(element: T): void {
        this.addElementAtLast(element); 
    }
    offer(element: T): boolean {
        try {
            this.addElementAtLast(element) ; 
            return true ;  
        } catch (error) {
            return false ; 
        }
        
    }
    
    poll(): T | null {
        try {
            const result = this.removeElementAtFirst() ; 
            return result ; 
            
        } catch (error) {
            return null ; 
        }

    }

    remove(): T {
        const result = this.removeElementAtFirst() ; 
        return result ; 
    }

    extends(elements:T[]):void{
        for (const value of elements){
            this.add(value) ; 
            console.log("!------------------------------->");
            console.log("Head ......");
            console.log('Prev: ',this.head?.prev, 'Data: ', this.head?.data,'Next: ', this.head?.next );
            console.log("Tail .......");
            console.log('Prev: ',this.tail?.prev,  'Data: ', this.tail?.data,  'Next: ',  this.tail?.next );
            console.log("!------------------------------->");
            
        }
    }

    peek(): T | null {
        const result:T | undefined = this.head?.data
        return result ? result : null ; 
    }
    lastPeek():T| null{
        const result:T | undefined = this.tail?.data
        return result ? result : null ; 
    }
    element(): T {
        if (this.head === null){
            throw new Error("The queue is empty")
        }

        const result = this.head.data ;
        return result ;  
        
    }



    //->>>> min-helpers
    empty(): boolean {
        return this.head === null ; 
    }

    //properties
    get size():number{
        return this.Size ; 
    }


}


//tried to this challenge 6/11/2025
function translatePossessed (message: string): string {
  // Your code here...

  if (message.trim() === '')return '' ; 

  let wordsArray: string[]  = message.split(' ') ; 
  let normalWords:string[] = wordsArray.map(word=>{
    let normal:string = word.split('').reverse().join('') ;

    return normal ; 
  }) ; 

  let result :string = normalWords.join(' ') ; 
  return result ; 
}

let messages:string[] = ['i yojne gnihctaw uoy',
'siht si gnorw','siht si gnorw','dooG secitcarP'] ; 
messages.forEach(v=>{
  console.log(translatePossessed(v)) ;
})




function countSheep(letters: string): number {
    letters = letters.toLowerCase() ; 
    function Counter<T>(data:T[]):Map<T, number>{
        const counter = new Map<T,number>() ; 
        const setter = (key:T,value:number)=>counter.set(key,value) ; 
        data.forEach(value=>{
            let currentNumber: number | undefined = counter.get(value); 
            if (currentNumber === undefined){
                setter(value,1); 
                return ; 
            }
            currentNumber++; 
            setter(value,currentNumber) ; 
        })
        return counter ; 
    }
    

    const counter = Counter(letters.split('') ) ; 
    let times:number = 0 ; 
    let keep:boolean = true ; 
    function getSheep():boolean{
        const get = (key:string):number|undefined  =>counter.get(key); 
        
            let s = get('s'); 
            let h = get('h'); 
            let e = get('e'); 
            let  p = get('p'); 

            if (e === undefined  || s === undefined|| h === undefined || p === undefined)return false ; 

            if (e < 2 || s < 1 || h < 1 || p < 1)return false ; 
            counter.set('s',s--); 
            counter.set('h',h--); 
            counter.set('e',e - 2); 
            counter.set('p',p--); 
            return true ;    
    }

    while(keep){
        if(getSheep()){
            times++; 
            continue ; 
        }
        keep = false ; 
    }
    

    // Your code here...
    return times ; 
}


let w = ["sheepxsheepy",'sshhheeeepppp', 'hola','peesh' ]

  w.forEach(v=>{
    console.log(v,countSheep(v))
  })



let a = new Array<number>(1,2,3,4,5).reduce((prev,next,index,array)=>{
    //console.log('prev: ',prev);
    //console.log('next: ', next);
    
    return prev + next ; 

})

console.log(a); 
let b = new Array<string>("hersy","Craice","Miseru","Ashely").reduce((prev,next)=>{
    if('Hello'=== prev)return '' ; 
    return prev + '--' + next 

},'Hello'); 
console.log(b);


let c:string[] =  new Array<string>("hersy","Craice","Miseru","Ashely"); 
Object.bind ; 
Object.apply  ; 
Object.call  ; 
let d = Object.getPrototypeOf(Stack) ; 
console.log(d);


/**
 7/011/2025
 HOW TO USE DEBUGGER 

 */





