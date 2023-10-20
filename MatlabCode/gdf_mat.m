clear all
path_open = 'G:\NoGitWork\DATA\MIdataset\BCI_IV_2a_gdf\';
path_save = 'G:\Git_Repository\MATLAB\EEG_Riemannian\data\BCI_IV_2a\';
subject = strcat(path_open,'A01E.gdf');
% cd('G:\Git_Repository\MATLAB\EEG_Riemannian\MatlabCode\biosig-2.5.1-Windows-64bit\share\matlab')
[data, h] = sload(subject, 0, 'OVERFLOWDETECTION:OFF');
n = find(h.EVENT.TYP == 768);
start = h.EVENT.POS(n);

fs = 250;
trial = length(n);
channel = 25;
len = 4*fs; % 2-6s
No_trial = zeros(trial,channel,len);

for t = 1:trial
    one_trial = data(start(t):start(t)+4*250-1,:);
    No_trial(t,:,:) = one_trial';
    % No_trial = No_trial(h.Classlabel,);
end
Data = No_trial;
class_return = h.Classlabel;
%% remove artifact
m = find(h.ArtifactSelection == 1);
Data(m,:,:) = [];
class_return(m,:) = [];
%% move window 7*250
time = 4;
L = 2*time-1;
data_return = zeros(length(class_return),channel,L*fs);
for w = 1:L
    data_return(:,:,(w-1)*(fs/2)+1:(w+1)*(fs/2)) = Data(:,:,(w-1)*(fs/2)+1:(w+1)*(fs/2));
end
%% save
subject = 1;
name = strcat('A0',int2str(subject),'E.mat');
save([path_save,name],'data_return','class_return');