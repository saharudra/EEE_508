img1=imread('cameraman.jpg');
m = mean(img1(:));
figure(1);
imshow(img1);
H=[1/9,1/9,1/9;1/9,1/9,1/9;1/9,1/9,1/9];
figure,imshow(H);
Y1=conv2(double(img1),double(H));

figure,imshow(Y1,[]);
Y2=filter2(H,img1);
figure,imshow(Y2,[]);
type filter2;
[S, HCOL, HROW] = isfilterseparable(H);

%H is a low pass filter since we are taking mean of the surrounding
%neighbours which will eliminate the pixel if it is not a representative of
%its surrounding thus eliminating that pixel
H3 = firlp2hp(H);
figure,imshow(H3);
H2=9.*[-1/9,-1/9,-1/9;-1/9,8/9,-1/9;-1/9,-1/9,-1/9];
Y4=conv2(double(img1),double(H2))+mean2(img1);
newm=mean(Y4(:));
figure,imshow(Y4,[]);
