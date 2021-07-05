public class LeapYearCheker {
    public static void main(String[] args) 
    {
        int year;
        for(int i=1;i<=2030;i++)
        {
            if (year % 4 == 0 && year % 100 != 0 || year % 400 == 0)
            {
                System.out.println(year+" is a leap year.");
            }
        }
       
    }
}
    