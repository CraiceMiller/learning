public enum CharacterNames {
    MEGUMIN("Megumin"), 
    KAZUMA("Kazuma");

    private final String currentName;
    CharacterNames(String currentName){
        this.currentName = currentName;
    }

    public String getName(){
        return this.currentName;
    }
        
}
