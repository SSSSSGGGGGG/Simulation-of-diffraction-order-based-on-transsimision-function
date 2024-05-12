syms  phi
%a=linspace(0,1,0.1)
a=0.9
f0=a^2*(cos((phi/2)*pi)^2)
f1=a^2*(sinc((a/2))^2)*(sin((phi/2)*pi)^2)
% Solve for phi
solutions = solve(f0 - f1, phi);

mod(double(solutions),2)

