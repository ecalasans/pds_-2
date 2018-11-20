load('/Users/ericcalasans/Documents/Estudos/Python/pds_P2/xa_12_1.sod')

xa = x_a;

k = 1:length(xa);

Xk = fft(xa);

k2 = 1:25:length(xa);

xa2 = xa(k2);

Xk2 = fft(xa2);

plot2d3(k2, Xk2)
