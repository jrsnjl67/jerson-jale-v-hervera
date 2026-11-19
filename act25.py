#??


Leg_Press = "The leg press is a lower-body compound weight training\n \
exercise where you push a weighted platform or sled away from\n \
your body by extending your legs against resistance. It trains\n \
multiple joints and muscle groups at once while supporting your\n \
back on a seat or pad."
Bulgarian_Split_Squats = "The Bulgarian split squat is a single-leg\n \
(unilateral) lower-body exercise performed with your rear\n \
foot elevated on a bench or raised surface while your front\n \
leg lowers your body into a squat or deep lunge.\n \
Most of your body weight stays on the front leg, building\n \
unilateral strength, balance, and hip mobility with less\n \
lower-back strain than heavy bilateral squats."
Step_ups = "A step-up is a unilateral lower-body exercise where\n \
you place one foot onto a raised surface—such as a box,\n \
bench, step stool, or stair—and drive through that lead\n \
leg to lift your body up before stepping back down."
Squat = "A squat is a fundamental compound lower-body exercise\n \
where you lower your hips from a standing position and then push back up."

Vastus_Medialis = [Squat, Step_ups,Bulgarian_Split_Squats,Leg_Press]#4
quad_parts = ["Rectus Femoris","Vastus Lateralis", Vastus_Medialis, "Vastus Intermedius"]#3
free_weight = ["dumbell press",quad_parts,"lat pulldown"]#2
gym = [free_weight,"calisthenics","hyrox","martial arts"]#1

print(gym[0][1][2][1])