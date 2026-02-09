//############################################## TYPES #####################################################
type StatsProps = {
    Hp:number,
    Str:number,
    Mag:number,
    Skill:number,
    Spd:number,
    Lck:number,
    Def:number,
    Res:number
}

type WeaponProps = {
    kind:"Sword" | "Lance" | "Axe" | "Bow" | "Tome" |"Staff"|"Other", 
    Mt:number,
    Hit:number, 
    Crit:number, 
    Rng:"1"|"2"|"1-2" , 
    Wt:number

}
type CharacterProps = {
    name : string, 
    gender: "Male" | "Female"|null, 
    stat : StatsProps, 
    weapon: WeaponProps | null, 
}

type  S = {
    Attack:number, 
    AvoidRate:number, 
    HitRate:number, 
    CriticalRate:number, 


}

//############################################## CLASS #####################################################

class Game{
    


    public random(min:number,max:number):number {
        return Math.floor(Math.random() * (max - min + 1) + min  )
        
    }

    public getStadistic(attacker:CharacterProps,target:CharacterProps|undefined):S{

        
        //ATK: Attack
        
        let Attack:number ; 



        if (attacker.weapon?.kind === "Tome" || attacker.weapon?.kind === "Staff"){

            Attack= attacker.stat.Mag + attacker.weapon.Mt - (target?.stat.Res || 0 )

        }else{
            Attack= attacker.stat.Str + (attacker.weapon?.Mt|| 0 ) - (target?.stat.Def || 0 )
        }

    
        


        //AVO: Avoid
        const AvoidRate: number = target? (target?.stat.Spd + target?.stat.Lck) - (target?.weapon?.Wt || 0):0 ; 



        //Hit: Hit rate
        const HitRate:number = (attacker.stat.Skill * 2 + (attacker.weapon?.Hit|| 0)) - AvoidRate ; 



        //CRIT: Critical rate:
        const CriticalRate:number = (attacker.stat.Skill + (attacker.weapon?.Crit || 0) ) - AvoidRate; 

        return {
            Attack,AvoidRate,CriticalRate,HitRate
        }
    }

    public willSurvive(attacker:CharacterProps,target:CharacterProps):boolean{
        const INFO:S = this.getStadistic(attacker,target) ; 
        return (target.stat.Hp - INFO.Attack ) > 0 ; 

    }

   



    /**
     * attack
    attacker
    targer    */
    public attack(attacker:CharacterProps,target:CharacterProps ):void {


        if (!attacker.weapon){
            console.log(`${attacker.name} has no weapon to use... `); 
            return ; 
        }

        const INFO:S = this.getStadistic(attacker,target) ; 




        //Calaculating the conditions to give the attack
        if (this.random(1,100) > INFO.HitRate){
            console.log(` "${attacker.name.toLocaleUpperCase()}" missed the attack `)
            return  
        }


        

        if((this.random(0,100) <= INFO.CriticalRate) ){
            target.stat.Hp -= INFO.Attack * 3

            console.log(`${attacker.name} lands a CRITICAL hit for ${target.name} !!!! `)
            return ;

        }

        target.stat.Hp -= INFO.Attack
        console.log(`${attacker.name} attacks to ${target.name}`)

    }



}



//########################################### WEAPONS ########################################################
const SilverSword:WeaponProps = { 
    kind:"Sword", 
    Mt:13,
    Hit:106, 
    Crit:4, 
    Rng:"1", 
    Wt:5
}

const SilverAxe:WeaponProps = { 
    kind:"Axe", 
    Mt:14,
    Hit:80, 
    Crit:0, 
    Rng:"1", 
    Wt:7
}
const Heal:WeaponProps = { 
    kind:"Staff", 
    Mt:14,
    Hit:80, 
    Crit:0, 
    Rng:"1", 
    Wt:7
}

const SilverLance:WeaponProps = { 
    kind:"Lance", 
    Mt:13,
    Hit:90, 
    Crit:0, 
    Rng:"1", 
    Wt:6
}

//######################################### CHARACTERS ##########################################################
const Ogma:CharacterProps={
    name:"Ogma", 
    gender:"Male", 
    stat:{
        Hp:54, 
        Str:23, 
        Mag:1, 
        Skill:22, 
        Spd:26, 
        Lck:17, 
        Def:16, 
        Res:3
    }, 
    weapon:SilverSword
}

const Minerva:CharacterProps={
    name:"Minerva", 
    gender:"Female", 
    stat:{
        Hp:30, 
        Str:14, 
        Mag:0, 
        Skill:11, 
        Spd:16, 
        Lck:15, 
        Def:17, 
        Res:3
    }, 
    weapon:SilverAxe
}

const Marth:CharacterProps={
    name:"Marth", 
    gender:"Male", 
    stat:{
        Hp:24, 
        Str:8, 
        Mag:0, 
        Skill:7, 
        Spd:9, 
        Lck:12, 
        Def:8, 
        Res:0
    }, 
    weapon:SilverSword
}

const Shiida:CharacterProps={
    name:"Shiida", 
    gender:"Female", 
    stat:{
        Hp:25, 
        Str:12, 
        Mag:1, 
        Skill:20, 
        Spd:20, 
        Lck:20, 
        Def:10, 
        Res:6
    }, 
    weapon:SilverLance
}

const Nabari:CharacterProps={
    name:"Nabari", 
    gender:"Male", 
    stat:{
        Hp:41, 
        Str:9, 
        Mag:0, 
        Skill:15, 
        Spd:20, 
        Lck:15, 
        Def:11, 
        Res:0
    }, 
    weapon:SilverSword
}

const Lena:CharacterProps={
    name:"Lena", 
    gender:"Female", 
    stat:{
        Hp:18, 
        Str:0, 
        Mag:7, 
        Skill:12, 
        Spd:13, 
        Lck:18, 
        Def:3, 
        Res:18
    }, 
    weapon:Heal
}


function main():void{
    
    const Dragon:CharacterProps = {
        name:"Dragon", 
        gender:"Male", 
        stat:{
            Hp:75, 
            Str:25, 
            Mag:7, 
            Skill:16, 
            Spd:20, 
            Lck:10, 
            Def:20, 
            Res:15
        }, 
        weapon:{ 
            kind:"Other", 
            Mt:20,
            Hit:101, 
            Crit:3, 
            Rng:"1-2", 
            Wt:14
        }
        
    }
    const players:CharacterProps[] = [Ogma,Minerva,Marth,Shiida,Nabari,Lena]


    const game = new Game()

    console.log("------------------------->")
    players.forEach(element=>{
        console.log(`${element.name} Stadistics: `, game.getStadistic(element,undefined))
    }

    )
    console.log("------------------------->")

    console.log("------------------------->")
    players.forEach(element=>{

        const getplayer = ():CharacterProps=>{
            let result = players[game.random(0,players.length - 1) ] ; 
            if (result=== undefined){
                throw new ReferenceError("The array is currently empty")
            }

            return result 
        }

        const  p = getplayer(); 

        console.log(`${element.name}  vs ${p.name}: `, game.getStadistic(element,p)); 
        console.log(`${p.name} will survive to ${element.name}'s attack ?:  `, game.willSurvive(element,p))
    }

    )
    console.log("------------------------->")

    console.log("Ogma", game.getStadistic(Ogma,Minerva))
    console.log("Minerva",  game.getStadistic(Minerva,undefined))
    console.log("Ogma", game.getStadistic(Ogma,undefined))
    console.log("Minerva will survive with the Ogma attack ? : ",  game.willSurvive(Ogma,Minerva))


    if (false){
        

    while (players.some(e=>e.stat.Hp > 0 ) && Dragon.stat.Hp > 0 ){
        console.log("-----------------------------------------------------------")
        console.log(`${Ogma.name}: HP ${Ogma.stat.Hp} / 54`)
        console.log(`${Minerva.name}: HP ${Minerva.stat.Hp} / 30`)
        console.log(`${Dragon.name}: HP ${Dragon.stat.Hp} / 75`)
        console.log("-----------------------------------------------------------")
        console.log("")
        console.log("------------------Character turn -------------------------")

        players.forEach(character =>{
            if (character.stat.Hp <= 0){
                return ; 
            }

            game.attack(character,Dragon)
        }
        )
        





        console.log("---------------------Dragon Turn ----------------------------")
        if( Dragon.stat.Hp <= 0){
            break ; 
        }

        const getplayer = ():CharacterProps=>{
            let result = players[game.random(0,players.length - 1) ] ; 
            if (result=== undefined){
                throw new ReferenceError("The array is currently empty")
            }

            return result 
        }

        try {
            game.attack(Dragon,getplayer())
            
        } catch (error) {
            break ; 
            
        }
 

    }
    console.log("-----------------------------------------------------------")
    console.log(`${Ogma.name}: HP ${Ogma.stat.Hp} / 54`)
    console.log(`${Minerva.name}: HP ${Minerva.stat.Hp} / 30`)
    console.log(`${Dragon.name}: HP ${Dragon.stat.Hp} / 75`)
    console.log("-----------------------------------------------------------")

    console.log(Dragon.stat.Hp <=0 ? "The heroes won the battle, the peace in the land arrived once more time":"The dragon won...")

    }

    
 
}

main()
