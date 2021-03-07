# Question 8.2
t = 0.001
E0 = 1
S0 = 10
C0 = 0
P0 = 0
T = 0
E = [E0]
S = [S0]
C = [C0]
P = [P0]
dP = list()
while T <= 0.8:
    k_e1 = -100*E0*S0 + C0*750
    k_s1 = -100*E0*S0 + C0*600
    k_c1 = 100*E0*S0 - C0*750
    k_p1 = 150*C0
    E1 = E0 + k_e1*t*0.5
    S1 = S0 + k_s1*t*0.5
    C1 = C0 + k_c1*t*0.5
    P1 = P0 + k_p1*t*0.5
    k_e2 = -100*E1*S1 + C1*750
    k_s2 = -100*E1*S1 + C1*600
    k_c2 = 100*E1*S1 - C1*750
    k_p2 = 150*C1
    E2 = E0 + k_e2*t*0.5
    S2 = S0 + k_s2*t*0.5
    C2 = C0 + k_c2*t*0.5
    P2 = P0 + k_p2*t*0.5
    k_e3 = -100*E2*S2 + C2*750
    k_s3 = -100*E2*S2 + C2*600
    k_c3 = 100*E2*S2 - C2*750
    k_p3 = 150*C2
    E3 = E0 + k_e3*t
    S3 = S0 + k_s3*t
    C3 = C0 + k_c3*t
    P3 = P0 + k_p3*t
    k_e4 = -100*E3*S3 + C3*750
    k_s4 = -100*E3*S3 + C3*600
    k_c4 = 100*E3*S3 - C3*750
    k_p4 = 150*C3
    # average slope
    k_e = (k_e1 + 2*k_e2 + 2*k_e3 + k_e4)/6
    k_s = (k_s1 + 2*k_s2 + 2*k_s3 + k_s4)/6
    k_c = (k_c1 + 2*k_c2 + 2*k_c3 + k_c4)/6
    k_p = (k_p1 + 2*k_p2 + 2*k_p3 + k_p4)/6
    Et = E0 + k_e*t
    St = S0 + k_s*t
    Ct = C0 + k_c*t
    Pt = P0 + k_p*t
    dP.append(k_p)
    E.append(Et)
    S.append(St)
    C.append(Ct)
    P.append(Pt)
    E0 = Et
    S0 = St
    C0 = Ct
    P0 = Pt
    T = T + t


import matplotlib.pyplot as plt
sam = [0,1,4,9,16]
ling = [1,2,3,4,5]
fig,ax=plt.subplots()
ax.plot(E)
ax.plot(S)
ax.plot(C)
ax.plot(P)
plt.show()


S.pop()
S = S[3:]
dP = dP[3:]
plt.scatter(S,dP)
plt.show()
