#include "mbed.h"

DigitalOut led1(LED1);
DigitalOut led2(LED2);
DigitalOut led3(LED3);

Serial pc(SERIAL_TX, SERIAL_RX);

const int N = 4;
int led_record[N];
//array declared to record
int number_of_button_pressed=0;
int *ptr[N];
int i;

int t;

Timeout button_debounce_timeout;
float debounce_time_interval = 0.3;
//debouncing button press

InterruptIn button(USER_BUTTON);

void onButtonStopDebouncing(void);

void onButtonPress(void)
{ 
    {      //for(i = 0; i < N; i++){
            
            led_record[i] = t;
            i++;
            number_of_button_pressed++;
            pc.printf("Number of button pressed is %d \r\n",number_of_button_pressed);

            }
        button.rise(NULL);
        button_debounce_timeout.attach(onButtonStopDebouncing, debounce_time_interval);

}

void onButtonStopDebouncing(void)
{
        button.rise(onButtonPress);
}

void select_led(int l)
{
        if (l==1) {
                led1 = true;
                led2 = false;
                led3 = false;
        }
        else if (l==2) {
                led1 = false;
                led2 = true;
                led3 = false;
        }
        else if (l==3) {
                led1 = false;
                led2 = false;
                led3 = true;
        }
}//function for cycling leds

void turn_playback (int s){
        if (s==1) {
                led1 = true;
                led2 = false;
                led3 = false;
        }
        else if (s==2) {
                led1 = false;
                led2 = true;
                led3 = false;
        }
        else if (s==3) {
                led1 = false;
                led2 = false;
                led3 = true;
        }
}


int main() {
        // attach the address of the callback function to the rising edge
        button.rise(onButtonPress);
         t=0;
         while(true) {
                select_led(t);
                wait(1);
               //pc.printf("Blink!Current cycling colour is %d \r\n",select_led(t));
                t=(t%3)+1;
                          
                if(number_of_button_pressed==4){
                    int counter =0;            
                    while(true){
                          turn_playback(led_record[counter]);
                          wait(1);
                          pc.printf("Playback sequence colour is %d \r\n",led_record[counter]);

                          counter++;
                          if(counter==4){counter=0;}

                          }
                    }
            }
        }
        