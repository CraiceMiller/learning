//____________________________________TASK CLASS TO DO _________________________
class Task {	
	#task;
	#id;
	#toDo;
	#length;

	static uniqueid = 101;
	constructor(taskName = "task",length = 1,taskToDo = null){
		this.#task = taskName; 	
		this.#id = Task.uniqueid;
		this.#toDo = taskToDo; 
		this.#length = length;
		
		Task.uniqueid += 1;
	}


	do(...values){	
		if (this.#toDo === null ) {console.log("No task to do");return }

		console.log(`Doing:    ${this.#task} `);
		if (values <= 0){
			this.#toDo();
			return 
		}

		this.#toDo(...values);

	}


	
	get id(){	
		return this.#id;
	}

	get length(){
		return this.#length;
}


}

//____________________________________BINARY SEARCH _________________________

function binary( Array, target) {
	let start = 0 ; 
	let end =Array.length - 1 ; 

	while (start <= end ) {
		let mid = Math.trunc(( start + end ) /2);

		if (Array[mid] === target ) { return  mid }

		else if(Array[mid] < target ) {start = mid + 1 }

		else {end = mid -1 }

	}
	return -1

}


//____________________________________MODIFY BINARY SEARCH _________________________

function modifyBinary( Array, target,start = 0, end = 0) {

	while (start <= end ) {
		let mid = Math.trunc(( start + end ) /2);

		if (Array[mid] === target ) { return  mid }

		else if(Array[mid] < target ) {start = mid + 1 }

		else {end = mid -1 }

	}
	return -1

}


//____________________________________TASK DOING _________________________

function toDo(task) {	
	task.do()
	return  task.length -1
}


/** 
*@param {array} arrayTask This is just the unique taskst to do
*@param {array}  arrayToDo This is just a sorted array of repeteated id
*@returns {void}

*/
function searchTask(arrayTask,arrayToDo){

	
	//1. Setting the values needed here...
	let currentIndex = 0;
	let taskIndex = 0; 
	let currentTask;
	let ToDoUniqueID;

	
	//2. This only do the very first task...
	currentTask = arrayTask[ taskIndex ];

	ToDoUniqueID = arrayToDo[ currentIndex ];
	
	currentIndex += toDo( currentTask) ;

	
	
	//           20     <=  78
	//3. Creating the loop to do the rest tasks
	while(currentIndex <= arrayToDo.length ) {

		//4. Confirmining that the in the moment when we add the step 
		//of the length. it is in fact the same!

		currentTask = arrayTask[ taskIndex ]; //index= 3, task= No.4
		ToDoUniqueID = arrayToDo[ currentIndex ]; //index= 20



		
		//5. this follow the next task, eg. task1 conver into task2
		if (currentTask.id === ToDoUniqueID) {

			taskIndex++;
			currentTask = arrayTask[ taskIndex ];

			//6. this only move to the next index (file)
			currentIndex++;


			
			// 7. Just do the task without do it more than one time...
			currentIndex += toDo(currentTask);


		}else{
			currentIndex -= currentTask.length;
			let findIndex = modifyBinary(arrayToDo,ToDoUniqueID,currentTask.length, currentIndex );

		




		}


		
		
		




















}





//Just waitingif i need this later... :|
/**

		if (currentTask.length === 1 ){ 
			currentIndex += toDo( currentTask, currentIndex ) ;
			taskIndex++;
			continue
		}

*/




//_____________________TESTING______________________________________
const work = () => {console.log("Doing Task...");setTimeout(()=>console.log("Done"),2000) };
const print = function (...values){console.log(...values)};
const task1 = new Task("Do something",4,work);
const task2 = new Task("Searching",6,work);
const task3 = new Task("Get the number task!!",2,work);
const task4 = new Task("Work",10,work);
const task5 = new Task("Meeting",7,work);
const task6 = new Task("Eat",1,work);
const task7 = new Task("KEEP WORKING ",14,work);
const task8 = new Task("PRESENTATION ",9,work);
const task9 = new Task("PAPERWORK",24,work); 

let taskToDo =[101, 101, 101, 101, 102, 102, 102, 102, 102, 102, 103, 		       		103, 104, 104, 104, 104, 104, 104, 104, 105, 105, 105,    	       		105, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106,
	       106, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107,
	       107, 107, 107, 107, 108, 108, 108, 108, 108, 108, 108, 		       		108, 108, 109, 109, 109, 109, 109, 109, 109, 109, 109, 		       		109, 109, 109, 109, 109, 109, 109, 109, 109, 109, 109, 		       		109,];

let allTasks =[task1,task2,task3,task4,task5,task6,task7,task8,task9 ];

print(task1.id);
print(task3.id);
task4.do();
print(task5.length);
searchTask(allTasks,taskToDo);

