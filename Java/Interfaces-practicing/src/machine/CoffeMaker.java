package machine; 

public class CoffeMaker implements ISmartDevice {
    private boolean isActive = false; 
    @Override
    public void turnOff() {
        // TODO Auto-generated method stub
        this.isActive = false; 
    }
    
   @Override
   public void turnOn() {
    // TODO Auto-generated method stub
    this.isActive = true;
   }
}
