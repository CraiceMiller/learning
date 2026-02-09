package machine;

/**a very simple gps ingine */
interface IGPS {
    abstract void getTargetLocation();
}

class GPS implements IGPS 
{
    @Override
    public void getTargetLocation() {
        // TODO Auto-generated method stub
        System.out.println("getting the location");        
    }
}