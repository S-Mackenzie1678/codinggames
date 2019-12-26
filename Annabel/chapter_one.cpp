#include "chapter_one.h"

void chapter_one() {
	for(int i; i <= 50; i++) {
		std::cout << "\n";
	}
	std::cout << "The road stretches away to the horizon before you. The heat from the desert makes the air wave in the distance. This is the start, and you don't remember what came before. The road stretches ahead." << std::endl;
	std::string walk = "w";
	while(walk != "w") {
		std::cout << "Press w to begin walking." << std::endl;
		std::cin >> walk;
		if(walk != "w") {
			std::cout << "It is natural to be wary. You may take as much time as you need." << std::endl;
		}
	}
	std::cout << "You walk. As you walk, the air is still and the ground is firm. As you walk, you notice mountains on the horizon that you hadn't seen before. As you walk, you realize that the Sun's light is making you thirsty. The desert does not seem too keen to provide water. As you ponder the predicament, you notice that you've been carrying a pouch filled with water the entire time. How didn't you notice it? You are confused, and wonder if you should take a sip from the appearing container." << std::endl;
	int refusals = 0;
	while(walk != "e") {
		std::cout << "Press e to have a drink." << std::endl;
		std::cin >> walk;
		if(walk != "e") {
			std::cout << "It makes sense that you doubt the beverage. It has just appeared, seemingly anyway. However, you will need a drink eventually, and knowing the water's habit of appearing, who knows if it'll ever disappear." << std::endl;
			refusals ++;
		}
		if(refusals == 5) {
			std::cout << "You might be smart to refuse the mysterious drink, but you would be smarter to take your chances at this point. You are very thirsty." << std::endl;
		}
		if(refusals > 5) {
			std::cout << "Trying to resist the urge to have a drink is exhausting. So much so that you lie down on the road. 'Just a little nap,' you tell yourself. 'Just a nap.'" << std::endl;
			for(int j; j <= 50; j++) {
				std::cout << "\n";
			}
			std::cout << "This journey has ended. It may have just been time for it to end, though. Of course, you may keep journeying another time." << std::endl;
			exit(0);
		}
	}
    std::cout << "You are no longer thirsty, but now you have nowhere to put the pouch. You don't want to litter; the desert is so pristine and it'd be a shame to ruin it. However, as you turn it over in yor hands, you notice writing on the back. There's no way you could have missed it, but it couldn't've just appeared, so you are puzzled. Upon regaining your composure, you read the text. It reads \"Lll'ihyihyi\". You don't know what it means. When you fix your attention on the road again, you see something that makes you happy. It's a road sign." << std::endl;
    std::cout << "The road sign's number is 19564." << std::endl;
    action_runner("r", "to continue", "As much as it ma frustrate, the end of a piece is just as needed as the beginning.");
    for(int k = 1; k <= 60; k++) {
        std::cout << "\n";
    }
    std::cout << "End of chapter one." << std::endl;
    std::cout << "Chapter special thanks: Adam Hutchings - Pull Request Merging" << std::endl;
    std::cout << "                        Liam Morris and Evan Morris - Motivation" << std::endl;
}
