Inventor of Information theory: *Claude Shannon*

Fundamental Problem Defined by Shannon: *The task of reliable communication over an unreliable channel*

Examples of *channels:* 
$my \ voice \rightarrow^{air} \ your \ ear$ // $medium = air$

$our \ eyes \rightarrow^{electrical \ signals} brain$ 

$antenna \leftrightarrow^{vacuu,} mars \ rover$ 

$phone1 \rightarrow^{copper \ wire} phone2$

In real life we have:
$Received \ Signal \approx Transmitted \ Signal + noise$


We would like to have communication systems where:
$Received \ Messgae = Transmitted \ Message$

Possible Solutions:
- Physical Solutions:
	- Where you throw away lousy systems and replace them with better built ones
		- Better wire on a phone line
		- A newer magnetic disk drive
- System Solutions:
	- Accept the lousy channel as it is and add encoding and decoding systems around that channel to turn it into a reliable channel
	- System approach accepts the system as it is and transforms it into a reliable system. 

$Source \ Message \rightarrow Encoder \rightarrow t \rightarrow Channel + noise \rightarrow Received \ Message \rightarrow Decoder \rightarrow \hat{s}$
$$
\begin{array}{}
s = Source \ Message \\
\hat{s} = Guessed/Decoded \ Source \ Message\\
t = Coded \ Transmission \\ 
n = Noise \\
r = Received \ Message \\ 
\end{array}
$$

Decoder will be a system for *inferring* $n$ and $s$

Toy Model:
*Binary Symmetric Channel:* 

$$
X = \begin{pmatrix}
0 \\ 
1
\end{pmatrix}
$$
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd} 


0 \arrow[r] \arrow[dr, rightarrow] & 0 \\ 

1 \arrow[r] \arrow[ur, rightarrow] & 1 \\

\end{tikzcd}

\end{document}
```
$$\begin{align*}
Assume\\
P(y = 0|x = 0) = 1-f\\
P(y=1|x=0)=f
\end{align*}$$
The probability that what comes out is what you put in is $1-f$ which might. be 90%.
The probability that it is not what you put in is $f$ or 10%

Whenever you put in a 0, there is a 10% chance a 1 will come out 
Whenever you put in a 1, there is a 90% chance a 0 will come out. 

Let's say we have invented a new disk drive, and testing has revealed that it flips *10% of bits* 
$$
\begin{align*}
f=0.1
\end{align*}
$$
is this a useful disk drive?

Question 1: A file of $N = 10,000 \ bits$ is stored, then read.
Roughly how many bits are flipped?
$$
\begin{align*}
1,000 \pm 100\\
\pm 900\\
\pm 30\\
Binomial Distribution\\
\sigma =standard \ deviation \\
variance = Npq=900=\sigma^{2}\\
mean= Np\\
p \rightarrow f\\
q \rightarrow 1-f
\end{align*}
$$
Answer:
$\boxed{1,000} \pm \boxed{30}$
This is too many bit flips

Question 2: For a sale-able disk drive
- 1 Gigabyte disk drive
- How small does $f$ need to be 

Possible $f$ values:
- $10^{-13} \sim$ every 1,000 times you fill the drive 
	- Let's say the drive has 5 years of use, at 1 gigabyte per day
	- $\#bits = 5 \ years \times 8 \times 10^{9} \ bits \ per \ day$ 
	- $= 5 \times 365 \times 8 \times 10^{9}bits$ 
	- $\approx 10^{13}$ 
- $10^{-5}$
- $10^{-3} \sim$
- $10^{-10}$

If we want a 1% chance of disappointment we would need an error probability of:
$f \approx 10^{-15}$ 
$1000 \ happy \ customers \rightarrow f \approx 10^{-18}$ if we want industry grade level of performance

We are aiming for $10^{-15}$ or better

*Example Encoders:* 
- Parity Coding: Take some string of 0's and 1's, say 8 bits, 1 byte, and add an extra bit that represents the sum of 1's, in a single binary digit.
  $$
  \{0,1,0,1,1,1,0,1|1\} \leftarrow last \ bit \ is \ parity
$$
There are *5*, *1's*, 5 is *odd*, so we have a 1 as our parity bit.
```tikz
\begin{document}
\begin{tikzpicture} 
\foreach \x in {1,2,...,5,7,8,...,12} 
{ 
\draw (\x,0) +(-.5,-.5) rectangle ++(.5,.5); 
} 

\end{tikzpicture}
\end{document}

```

- Repetition Coding: 
	- $R_{3}$ 
	- $s:0$
	- $t:000$ // repeated source three times
	- $0 \rightarrow 000$
	- $1 \rightarrow 111$
$$
\begin{align*}
s=01101\\
t=000 \ 111 \ 111 \ 111 \ 000 \ 111 \\
n=000 \ 100 \ 000 \ 101 \ 000\\
r=000 \ 011 \ 111 \ 101 \ 111\\
r=t \oplus n \ modulo \ 2

\end{align*}
$$
Decoder:
$$
\begin{align*}
r   & \rightarrow \hat{s}\\
000 & \rightarrow 0\\
011 & \rightarrow 0\\
110 & \rightarrow 1\\
111 & \rightarrow 1
\end{align*}
$$
Best of $N$ or Best of $3$ decoder 

Applying decoder here
$$
\begin{align*}
s=000 \ 011 \ 111 \ 101 \ 111\\
\hat{s} = 0 \ 1 \ 1 \ 1 \ 1
\end{align*}
$$
*Decoding is Inference*

*Inference:* to do inference we need to use inverse probability, and the rules of probability
1. Product Rule:
   $$\begin{align*}
P(s,r) = P(s)P(r|s)\\
=P(r)P(s|r)
\end{align*}
$$
2. Sum Rule:
   $$
   \begin{align*}
P(r) = \sum\limits_{s}P(s,r) = P(s=0,r)+P(s=1,r)&
\end{align*}
$$
"Posterior Probability of s:"
$$
\begin{align*}
&P(s|r) = \frac{P(r|s)P(s)}{P(r)}\\
&P(r)=P(r|s=0)P(s=0)+P(r|s=1)P(s=1)
\end{align*}

$$

Example:
$$
\begin{align*}
&r=011\\
&P(r|s=0)=(1-f)\times(f)\times(f) = (1-f)f^{2}//two\ bits \ flipped\\ 
&P(r|s=1)=(f)\times(1-f)\times(1-f)=f^{1}(1-f)//one\ bit \ flipped
\end{align*}
$$
$$
\begin{align*}
&P(s=0)=\frac{1}{2}\\
&and \ P(s=1)=\frac{1}{2}\\
&then \ P(s=1|r=011) = \frac{(1-f)^{2}f\frac{1}{2}}{(1-f)f^{2} \frac{1}{2}+f(1-f)^{2}\frac{1}{2}}=(1-f)
\end{align*}
$$
$$
\begin{align*}
r \rightarrow \hat{s}\\
011 \rightarrow P(s=1|r=011)\\
=1-f
\end{align*}
$$
$$
\begin{align*}
P(s=1|r)>P(s=0|r)
\end{align*}
$$





