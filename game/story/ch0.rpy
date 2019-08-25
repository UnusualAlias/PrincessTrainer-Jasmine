label ch0:
    default skip_next = "skip_to_ch1"
    call desert_0
    show bg bg1
    show screen skips
    show me tired at left with dissolve
    me "Phew..."
    me "Not even a tumbleweed!"
    me "I need to find somewhere new to collect wood."
    me "There's nothing but sand left here."
    show ev 01
    show me back at left with dissolve
    me "{size=45}Huh!?"
    me "That isn't a mirage."
    me "..."
    me "There's something shiny in the sand."
    hide me
    hide ev 01
    show bg cg1
    $ abdul.got(black_lamp,1,002)
    with dissolve
    me "An oil lamp?"
    me "Looks new..."
    me "It must be my lucky day! I can sell this and eat a full meal tonight."
    $ qlog.got(sell_lamp)
    show bg bg1
    show me confused at left
    with dissolve
    me "They say Aladdin found his Genie in one of these. They say he wished for all the things he has now."
    me "I wish I could believe those rumors."
    menu:
        "Rub the lamp!":
            hide me
            show bg cg2 with Dissolve(2)
            me "{size=45}What the fuck?"
            show bg bg1
            show me alert at left
            with dissolve
            show jaf genie at right
            with dissolve
            jaf "{size=45}Well, aren't you glad to be naive?"
            show me afraid at left
            $ msg.msg("You dropped your CamelThorns and the lamp")
            me "{size=45}Woah! {w=.6}Whoa. {w=.4}Wha {w=.2}Wa..."
            jaf "{size=45}Where are you running to?"
            me "{size=40}Please don't steal my soul."
            jaf "{size=40}Calm down, I'm not interested in your soul."
            me "{size=30}Are you? {w=.5}A... {w=.5}A Genie?"
            jaf "Is it that obvious? {w=.5}Here, let me just..."
            show jaf normal at right with dissolve
            jaf "That's better."
            show me confused at left
            me "Wait! {w=.8}Jafar?"
            jaf "In the flesh, {w=.5}or smoke. {w=.8}Fire to be precise."
            jaf "Yes,{w=.3} yes, {w=.3}Genies are made of fire."
            jaf "Pick up my lamp, would you?"
            show me alert at left
            me "{size=25}Sorry."
            show me bent at left
            $ msg.msg("You got the Black lamp.")
            show jaf thinking at right
            jaf "Abdul? {w=.8}Is that you?"
            show me confused at left
            jaf "Where's your belly you fat fuck? {w=.5}I didn't recognize you without it."
            jaf "And what are you doing in the middle of desert at this time of day?"
            jaf "Shouldn't you be selling fish in the bazaar?"
            show jaf normal at right
            show me sad at left
            me "Well... {w=.6}I can't do that anymore."
            me "Aladdin destroyed my fish stall in one of his fights."
            me "They blamed it on you returning to Agrabah. {w=.6}but..."
            me "Every other day he'd drag one of his problems into the bazaar."
            me "Breaking more of my fish barrels every single time. {w=.5}Those are expensive."
            me "I can't take my fish to the bazaar to sell without barrels."
            me "No fish to sell, {w=.4}no money to buy barrels, {w=.4}no money to buy fish food, {w=.4}no money to buy bread."
            show jaf thinking at right
            jaf "Well that explains your missing belly."
            me "And my fish pond dried up. Jafar. {w=.5}All of my fish died. {w=.8}I'm a firewood collector now."
            show jaf normal at right
            jaf "Agrabah is an oasis my friend. {w=.5}A drop of water in the middle of the scorching sands."
            show me normal at left
            jaf "I warned the Sultan about wasting too much of the drinkable water on his fountains and his garden."
            jaf "He never listened."
            jaf "Or never cared."
            jaf "Either way he's the one to blame. {w=.4}That mother fucking old piece of shit."
            me "..."
            show jaf thinking at right
            jaf "Hey, {w=.4}hows your mother?"
            show me sad at left
            me "She died."
            jaf "Damn, {w=.8}how long I was gone for? {w=.5}That old hag still had a solid ten years or so."
            me "Roughly a year."
            jaf "Is that so?"
            me "Yes, {w=.8}my mother died few months ago. Just after I lost my business."
            if not persistent.theme_change:
                show jaf looking at right
                me "She tried to help me out by working, but..."
                jaf "Hmmm..."
                me "Jafar?"
                show jaf normal at right
                jaf "Ah, {w=.5}sorry Abdul, I {w=.5}got distracted. Anyway..."
            else:
                me "She tried to help me out by working, but..."
                jaf "Ah? {w=.8}Well, you can tell me all about your misfortune later."
                show me confused at left
            show jaf thinking at right
            jaf "You do know what this means don't you?"
            show me confused at left
            me "What?"
            jaf "It means you're the hero of the story now!"
            me "The hero?"
            show jaf normal at right
            jaf "Yes my friend, {w=.5}down on your luck, {w=.5}dead mother and facing an unbelievable opportunity."
            jaf "Those are the telltale characteristics of a great story being written."
            jaf "This time, it's yours!"
            jaf "Abdul my friend, {w=.5}your life is about to change."
            if not persistent.theme_change:
                show jaf looking at right
                jaf "Speaking of change..."
                show jaf normal at right
            me "Opportunity?"
            show jaf disappointed at right
            jaf "Akh... {w=.8}alright I'll spell it out for you."
            show jaf normal at right
            jaf "I'm a Genie and your rubbed me out {w=.4}...heh..."
            jaf "Now I have to grant you three wishes."
            me "Really?"
            jaf "Yes, {w=.6}aren't you glad you rubbed it before selling my lamp?"
            me "How did you know that was my plan?"
            jaf "You have to stop talking to yourself out loud, my friend."
            show me alert at left
            jaf "You haven't gone crazy have you?"
            me "No!"
            show me confused at left
            jaf "Good, {w=.5}nobody actually does that. {w=.5}Any time you see somebody talking to themself, {w=.5}it's totally fake."
            show me embarrassed at left
            jaf "As I was saying: {w=.5}You make a wish and then I'll try to twist your words against you."
            show me alert at left
            me "Against me? {w=.5}But why?"
            show jaf thinking at right
            jaf "I think it's supposed to be about teaching you a lesson."
            jaf "The value of contentment or something unfathomably stupid like that."
            show jaf normal at right
            jaf "HOWEVER!"
            jaf "I have a deal to propose."
            if not persistent.theme_change:
                show jaf looking at right
                jaf "First though, {w=.5}let me do something about this ugliness."
                show jaf normal at right
                show me confused at left
                me "What ugliness?"
                jaf "Ah, {w=.5}right... You can't see it."
                jaf "Let me show you."
                show jaf magic at right
                show me alert at left
                me "What the..."
                jaf "With just a little touch up."
                $ persistent.theme_change = 1
                show jaf thinking at right
                jaf "It's still not finished yet, {w=.5}but better than that ugly wood."
                show jaf normal at right
                jaf "Much better, {w=.5}don't you think Abdul?"
                show me smug at left
                me "Gold?"
                jaf "Yes. {w=.5}Is there something wrong with it?"
                me "Haven't you heard what romans say about us?"
                jaf "That we love gold?"
                me "Yes, they're mocking us for it."
                jaf "Don't you like gold?"
                show me alert at left
                me "I do, {w=.5}but..."
                jaf "So they speak the truth, {w=.5}why should that bother me?"
                me "But it's hateful..."
                jaf "It's just the way they choose to see it. {w=.5}You humans do that for everything."
                jaf "Even if it's hate, {w=.5}I'll take spoken hate over hateful acts any day."
                show me confused at left
                me "You're right jafar, {w=.5}you mentioned a deal?"
                jaf "Ah, {w=.5}yes!"
            else:
                me "A deal?"
                jaf "Yes"
            jaf "If you promise to help me get my revenge on those three idiots..."
            jaf "The ones who trapped me in this thing."
            jaf "And let me decide what you wish for your first, {w=.5}and second wishes..."
            jaf "I'll tell you how to avoid being screwed for your last wish."
            show me confused at left
            me "Screwed?"
            jaf "It means, {w=.5}I'll kill you with your own wish."
            show me alert at left
            me "Wait I've heard Genies can't kill..."
            jaf "Not directly we can't, {w=.5}but you'll be surprised to know..."
            me "What you can't live through?"
            jaf "You've heard that one?"
            show me confused at left
            jaf "No! That was the old me..."
            jaf "I was about to say: {w=.5}How easy it is to let people die on their own."
            me "What do you mean?"
            menu:
                jaf "No time to explain. {w=.5}What do you say? {w=.5}Do we have a deal?"
                "...Sure?":
                    jaf "Excellent! Then let us head back to Agrabah."
                    $ qlog.got(jafars_revenge)
                    $ qlog.cancel(sell_lamp)
                    jaf "Bring the sticks, {w=.5}we'll need all the money we can get our hands on, for the moment, anyway."
                    $ msg.msg("You got CamelThorns")
                    jump ch1
                "No! I just want my wishes":
                    show me normal at left
                    jaf "Are you sure? {w=.5}That road doesn't end well for you my friend."
                    menu:
                        jaf "Last chance Abdul! Don't throw away this opportunity."
                        "I just want my wishes Jafar.":
                            jaf "So be it."
                            jump wishes
                        "Alright, alright, I yield, just don't screw me, whatever that means.":
                            jaf "Good, then let us make haste! {w=.5}Time's a wastin'."
                            $ qlog.got(jafars_revenge)
                            $ qlog.cancel(sell_lamp)
                            show me confused at left
                            me "What?"
                            jaf "It's a charming expression I picked up, {w=.5}alas, never mind."
                            jump ch1
        "Don't be naiive, {w=.5}let's just go back to the city.":
            jump endless_grind
