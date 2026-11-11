# Arm 1 — Reference answer — 05-tutoring case-29 (Correlation vs. Causation)

## 1. The misconception

The student believes **correlation implies causation** — that because two variables move together, one must be *causing* the other to change. Their reasoning ("the two variables move together, so one must be driving the other") assumes there are only two possibilities: either ice cream drives shark attacks, or nothing is going on. They've missed the third option: **both variables could be responding to a hidden third factor**, called a *lurking variable* or *confounding variable*. In this case, that variable is hot summer weather — when it's hot, more people buy ice cream AND more people swim in the ocean, which puts more people near sharks. Cutting ice cream sales wouldn't touch shark attacks at all, because ice cream isn't in the causal chain.

## 2. Explaining it to the student

Here's the key idea: **when two variables are correlated, there are three possible explanations** —

1. **A causes B**
2. **B causes A**
3. **C causes both A and B** (a lurking variable), or it's just coincidence

You can't tell which one just from the data moving together. You need to ask: *"Is there something else that could be pushing both of these up and down at the same time?"*

**Concrete example:** Suppose data shows that towns with more churches have more crime. Does that mean churches cause crime? No! The lurking variable is **population size** — bigger towns have more of everything: more churches, more crime, more pizza shops, more traffic lights. Shrinking the number of churches wouldn't reduce crime, because neither one causes the other.

Back to your problem: ice cream sales and shark attacks both spike in **summer**. Hot weather makes people buy ice cream, and hot weather sends people to the beach where sharks live. So the real chain looks like this:

> Hot weather → more swimmers in the ocean → more shark attacks
> Hot weather → more ice cream purchases

Ice cream and shark attacks are connected only through their shared cause. That's why "buy less ice cream" fails as a strategy — it doesn't interrupt anything in the actual causal chain. To reduce shark attacks, you'd need to change something that actually affects swimming behavior, like warning systems or beach patrols.

**Rule of thumb for similar problems:** whenever you see "X and Y rise and fall together," don't jump to "X causes Y." First hunt for a lurking variable that plausibly drives *both*.

## Quick check for the student (same idea, new problem)

**Problem:** A town notices that the more firefighters sent to a fire, the greater the fire damage in dollars. A council member proposes: "To reduce fire damage, we should send fewer firefighters."

Is the council member's reasoning sound? Identify the relationship and any lurking variable.

**Solution:** The reasoning is not sound — it confuses correlation with causation. Firefighters don't cause the damage; the **size/severity of the fire** is the lurking variable. Bigger fires cause more damage AND require more firefighters to be dispatched. The correct picture is:

> Big fire → lots of damage
> Big fire → many firefighters called

Sending fewer firefighters would likely make damage *worse*, not better. To find the true cause-and-effect here, you'd want to compare fires of similar size and see whether firefighter count still relates to damage — controlling for the lurking variable.