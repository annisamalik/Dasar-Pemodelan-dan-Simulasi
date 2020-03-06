clear all;
close all;
clc;

%Deklarasi global
g = -9.81;
c = 0.8; % koefisien restitusi

y0 = 0;
t = 0;
dt = 0.1;

sudut = 45;
sudut_rad = sudut*(pi/180);

%Inisialisasi kondisi awal untuk sistem TANPA RESISTENSI
  x = 0;
  y = 0;
  v0 = 20;

  %Initial state of x and y for analytics
  x_ex = 0;
  y_ex = 0;
  x_tik = 0;
  
  vx = v0*cos(sudut_rad);
  vy = v0.*sin(sudut_rad);
  
  

%INISIALISASI DENGAN RESISTENSI UDARA (Hukum Stokes)
  vs = 20;
  m = 1;  
  b=0.5; %koefisien stokes b = 3p?Dv 
  tau = m/b;
  x_tiks = 0;

  %Initial state of x and y for numerics with Stokes
  x_s = 0;
  y_s = 0;

  %Initial state of x and y for analytics with Stokes
  x_exs = 0;
  y_exs = 0;

  vx_s0 = vs*cos(sudut_rad);
  vy_s0 = vs.*sin(sudut_rad);

  a_y = (m*g-b*vy_s0) / m;
  a_x = (-b*vx_s0) / m;
  
  vx_s = vx_s0;
  vy_s = vy_s0;
  

figure;
for i=1:10
  
  subplot(2,2,1);
  plot(x ,y, 'ro');
  axis ([0 150 0 20]);
  ylabel('y[m]');
  title(['Solusi Numerik']);
  
  subplot(2,2,2);
  plot(x_ex,y_ex,'bo');
  xlabel('x[m]');
  ylabel('y[m]');
  title(['Solusi Analitik']);
  axis ([0 150 0 20]);
  
  pause(0.01);
  
  while (y>=0)
    %Analisis Numerik in ideal system
    vx = vx;
    vy = vy + g*dt;
    
    y = y + vy*dt;
    x = x + vx*dt;
    t = t + dt;
    
    %Analisis Analitik in ideala system
    x_ex = (v0 * cos(sudut_rad) * t) + x_tik;
    y_ex = ((0.5 * g * (t^2)) + (v0 * sin(sudut_rad) * t));   
    
    subplot(2,2,1);
    plot(x ,y, 'ro');
    hold on;
    axis ([0 150 0 20]);
    ylabel('y[m]');
    xlabel('x[m]');
    title(['Solusi Numerik']);
    
    subplot(2,2,2);
    plot(x_ex,y_ex,'bo');
    hold on;
    xlabel('x[m]');
    ylabel('y[m]');
    title(['Solusi Analitik']);
    axis ([0 150 0 20]);
    
    pause(0.01);
  end;
  
  %Analisis Analitik
  t = 0;
  x_tik = x_ex;
  
  %Kecepatan berkurang karena ada koefisien restitusi
  v0 = v0*c;
  vx = v0*cos(sudut_rad);
  vy = v0.*sin(sudut_rad);
  
  %inisialisasi tinggi menjadi 0
  y = 0;
  y_ex = 0;
  
  
end

t = 0;

for i=1:10
  y_s = 0;
  y_exs = 0;
    
  subplot(2,2,3);
  plot(x_s,y_s,'ro');
  xlabel('x[m]');
  ylabel('y[m]');
  title(['Solusi Numerik dengan Hk Stokes']);
  axis ([0 60 0 20]);
  
  subplot(2,2,4);
  plot(x_exs,y_exs,'bo');
  xlabel('x[m]');
  ylabel('y[m]');
  title(['Solusi Analitik dengan Hk Stokes']);
  axis ([0 60 0 20]);
  
  pause(0.01);
  
  while (y_s>=0)
    t = t + dt; 
    
    %Analisis numerik dengan Stokes's Drag
    temp_a_y = a_y;
    temp_a_x = a_x;
    a_y = g-(b/m)*vy_s;
    a_x = (-b*vx_s) / m;
    
    y_s = y_s + vy_s*dt;
    x_s = x_s + vx_s*dt;
    
    vx_s = vx_s + temp_a_x*dt;
    vy_s = vy_s + temp_a_y*dt;
    
    %Analisis analitik dengan Stokes's Drag
    %vx_sa = vx_s0*exp(-t/tau);
    %vy_sa = (g*tau) + (vy_s0 - g*tau )*exp(-t/tau);
    x_exs = x_tiks + vx_s0*tau*(1-exp(-t/tau));
    y_exs = 0 -(-g*tau*t)+(vy_s0 + -g*tau)*tau*(1-exp(-t/tau));
    
    subplot(2,2,3);
    plot(x_s,y_s,'ro');
    hold on;
    xlabel('x[m]');
    ylabel('y[m]');
    title(['Solusi Numerik dengan Hk Stokes']);
    axis ([0 60 0 20]);
    
    subplot(2,2,4);
    plot(x_exs,y_exs,'bo');
    hold on;
    xlabel('x[m]');
    ylabel('y[m]');
    title(['Solusi Analitik dengan Hk Stokes']);
    axis ([0 60 0 20]);
    
    pause(0.01);
  end;

  %Analisis Analitik
  t = 0;
  x_tiks = x_exs;
  
  %Kecepatan berkurang karena ada koefisien restitusi
  vs = abs((sqrt(vx_s^2+vy_s^2))*c);
  vx_s0 = abs(vs*cos(sudut_rad));
  vy_s0 = vs.*sin(sudut_rad);
  vy_s = vy_s0;
  vx_s = vx_s0;
  
end