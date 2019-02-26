/**
 * 
 * 
 * Clase tiempo implementada con clase nativa de java
 * @author d18sisaj
 *
 */
package segundatandaPOO;
import java.util.Calendar;
import java.time.LocalDateTime;
public class TiempoImplementado {

  public static void main(String[] args) {
    // TODO Auto-generated method stub
    LocalDateTime hora = LocalDateTime.now();
    /**
     * La funcion get"FOO" nos devuelve un entero normal y corriente
     */
    System.out.println(Integer.toString(hora.getHour())+" hora "+Integer.toString(hora.getMinute())+" minuto "+Integer.toString(hora.getSecond())+" Segundos");
    /**
     * La funcion plus"Medidadetiempo" devuelve una instancia de clase, para almacenar el incremento, simplemente
     * la igualo a la instancia original
     */
    hora=hora.plusHours(3);
    hora=hora.plusMinutes(40);
    hora=hora.plusSeconds(59);
    System.out.println(Integer.toString(hora.getHour())+" hora "+Integer.toString(hora.getMinute())+" minuto "+Integer.toString(hora.getSecond())+" Segundos");

    
  }
    
}
