filename1 = "~/Desktop/dataset/s1/s1_downstairs_nowall_trial1/A0_1_0/recording0_0_1.wav";
filename2 = "~/Desktop/dataset/s1/s1_downstairs_nowall_trial1/A0_1_0/recording0_0_3.wav";
[y1, fs1] = audioread(filename1);
[y2, fs2] = audioread(filename2);
[tau, R, lag] = gccphat(y1, y2, fs1);

fprintf('tau: %d\n', tau);

disp('R:')
disp(abs(R(1:100)))

disp('lag:')
disp(lag(1:2))