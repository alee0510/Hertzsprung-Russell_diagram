%import data
load MagnitudoVisual 
load Paralax
load BV
%B-V=BV
%calculation

%jarak
Jarak=1000./Paralax; %dalam parsec

%Magnitudo Mutlaks
M0=4.83; %magnitudo mutlak matahari
MagnitudoMutlak=(MagnitudoVisual)+5-5*log(Jarak); %magnitudomutlak bintang

%Luminositas (L=Lb/L0), L0=Luminositas Matahari, Lb= Luminositas Bintang
logLuminositas=(MagnitudoMutlak-M0)/-2.5; %Luminositas

%Temperatur
Temperature=4600*((1./(0.93.*BV+1.7))+(1./(0.92.*BV+0.62)));