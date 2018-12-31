% to read the stars data:
load onedata BV logLuminositas MagnitudoMutlak Temperature
load hiparcos O B A F G K M

%definisi data
mag=MagnitudoMutlak;

%Magnitudo
mA=mag(1:18568);
mB=mag(18569:28905);
mF=mag(28906:54277);
mG=mag(54278:76831);
mK=mag(76832:108664);
mM=mag(108665:113442);
mO=mag(113443:113650);

%Luminositas
LA=logLuminositas(1:18568);
LB=logLuminositas(18569:28905);
LF=logLuminositas(28906:54277);
LG=logLuminositas(54278:76831);
LK=logLuminositas(76832:108664);
LM=logLuminositas(108665:113442);
LO=logLuminositas(113443:113650);

%Temperature
tA=Temperature(1:18568);
tB=Temperature(18569:28905);
tF=Temperature(28906:54277);
tG=Temperature(54278:76831);
tK=Temperature(76832:108664);
tM=Temperature(108665:113442);
tO=Temperature(113443:113650);

%# plot
figure(1)
ax1 = gca;
line(O, LO, 'LineStyle', '.','Color', 'k', 'MarkerSize', 1);
line(B, LB, 'LineStyle', '.','Color', 'b', 'MarkerSize', 1);
line(A, LA, 'LineStyle', '.','Color', 'c', 'MarkerSize', 1);
line(F, LF, 'LineStyle', '.','Color', 'm', 'MarkerSize', 1);
line(G, LG, 'LineStyle', '.','Color', 'y', 'MarkerSize', 1);
line(K, LK, 'LineStyle', '.','Color', 'g', 'MarkerSize', 1);
line(M, LM, 'LineStyle', '.','Color', 'r', 'MarkerSize', 1);

ax2 = axes('Position',get(ax1,'Position'),...
           'XAxisLocation','top',...
           'YAxisLocation','right');
line(tO, mO, 'LineStyle', '.', 'Color', 'k', 'MarkerSize', 1);
line(tB, mB, 'LineStyle', '.', 'Color', 'b', 'MarkerSize', 1);
line(tA, mA, 'LineStyle', '.','Color', 'c', 'MarkerSize', 1);
line(tF, mF, 'LineStyle', '.','Color', 'm', 'MarkerSize', 1);
line(tG, mG, 'LineStyle', '.','Color', 'y', 'MarkerSize', 1);
line(tK, mK, 'LineStyle', '.','Color', 'g', 'MarkerSize', 1);
line(tM, mM, 'LineStyle', '.','Color', 'r', 'MarkerSize', 1);

%Label
xlabel(ax1,'B-V color')
ylabel(ax1,'LogLuminositas')
xlabel(ax2,'')
ylabel(ax2,'Absolute Magnitudo')