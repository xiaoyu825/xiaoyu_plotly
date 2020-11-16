#!/bin/bash
echo "[.] Processing $1"
echo "[.] Fetching Logs"

while IFS= read -r line
do
    if [[ $line == \#* ]]; then
        continue
    fi
    if [ -z "$line" ]; then
        continue
    fi
    desc=($line)
    if [[ ${desc[0]} == 14 ]]; then
        user=byl
        password=byl
    elif [[ ${desc[0]} == 6 ]]; then
        user=root
        password=gpv2r5VLo6fWoyrJgJLr
    elif [[ ${desc[0]} == jupyter ]]; then
        continue
    elif [[ ${desc[0]} == 17 ]]; then
        user=root
        password=ai_cv_lab_2020
        sshpass -p $password scp -o StrictHostKeyChecking=no -p $user@10.207.43.${desc[0]}:${desc[1]}/${desc[2]} ./logs/${desc[2]}
        continue
    elif [[ ${desc[0]} == 18 ]]; then
        user=root
        password=ai_cv_lab_2020
        sshpass -p $password scp -o StrictHostKeyChecking=no -p $user@10.207.43.${desc[0]}:${desc[1]}/${desc[2]} ./logs/${desc[2]}
        continue
    elif [[ ${desc[0]} == 19 ]]; then
        user=root
        password=ai_cv_lab_2020
        sshpass -p $password scp -o StrictHostKeyChecking=no -p $user@10.207.43.${desc[0]}:${desc[1]}/${desc[2]} ./logs/${desc[2]}
        continue
    elif [[ ${desc[0]} == 20 ]]; then
        user=root
        password=ai_cv_lab_2020
        sshpass -p $password scp -o StrictHostKeyChecking=no -p $user@10.207.43.${desc[0]}:${desc[1]}/${desc[2]} ./logs/${desc[2]}
        continue
    elif [[ ${desc[0]} == 04 ]]; then
         user=root
         password=aicvimage2019!
         sshpass -p $password scp -o StrictHostKeyChecking=no -p $user@10.207.174.${desc[0]}:${desc[1]}/${desc[2]} ./logs/${desc[2]}
         continue
    else
        user=root
        password=aicvimage2019!
    fi
    sshpass -p $password scp -o StrictHostKeyChecking=no -p $user@10.207.174.${desc[0]}:${desc[1]}/${desc[2]} ./logs/${desc[2]}
done < "$1"
echo "[.] Plotting Log"
/root/anaconda3/envs/imet/bin/python wplot.py $1 $1
echo "[x] Finished"
