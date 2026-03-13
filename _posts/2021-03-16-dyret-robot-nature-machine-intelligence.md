---
layout: post
title: "Shape-shifting robots in the wild: the DyRET robot"
date: 2021-03-16
category: posts
tags:
- research
- robotics
- machine learning
- artificial intelligence
description: "Our research on DyRET, a four-legged robot that adapts its body shape to walk on new terrain, has been published in Nature Machine Intelligence."
image: /assets/blog/2021/2021-dyret-robot.jpg
---

Imagine running on a cement footpath, and then suddenly through dry sand. Just to keep upright, you would have to slow down and change the way you run. In the same way, a walking robot would have to change its gait to handle different surfaces.

Generally, humans and most robots can only change *how* we run. But what if we could also change the shape of our bodies to run as fast and safely as possible on any surface?

We'd like to rely on robots for difficult and dangerous tasks — from inspecting failed nuclear reactors to space exploration. For these tasks, a static body could limit the robot's adaptability. A shape-shifting body could make the difference between success and failure in unexpected environments. Even better, a shape-shifting robot could learn the best body shape for different environments and adapt as it encounters new ones.

In a collaboration between the University of Oslo and CSIRO's Data61, we've successfully tested this idea with a four-legged robot that adapts its body to walk on new surfaces as it encounters them, performing better than a static-body robot. Our research is published in [*Nature Machine Intelligence*](https://doi.org/10.1038/s42256-021-00320-3).

![The DyRET robot walking outdoors on natural terrain]({% link assets/blog/2021/2021-dyret-robot.jpg %})

## A shape-shifting quadruped

DyRET — the Dynamic Robot for Embodied Testing, or "the animal" in Norwegian — was designed by Tønnes Nygaard to explore the idea of a shape-shifting robot. Each of DyRET's four legs has two telescopic sections, so it can change the length of its thigh or shin bones. The adjustments are made by motors built into the legs, and the lengths can be changed automatically while the robot is operating.

The motors can change DyRET's height by around 20%, from 60cm to 73cm tall. That 13cm makes a dramatic difference to the robot's walk. With short legs, DyRET is stable but slow, with a low centre of gravity. In its tallest mode, it is less stable but its stride is much longer, allowing it to travel faster and step over obstacles.

DyRET also has sensors to track what it's walking on. Each foot has a force sensor to feel how hard the ground is. A 3D camera points at the ground between its front legs to estimate how rough the surface is.

## Learning to adapt

When DyRET is walking, it continuously senses the environment through its feet and 3D camera. When the robot detects a change in ground conditions, it can switch to the best leg length. But how does it know what body shape works best?

We explored two ways for DyRET to learn the best leg configuration: controlled indoor tests with known surfaces, and real-world outdoor tests.

In the controlled tests, DyRET walked inside boxes about 5 metres long containing different surfaces: sand, gravel, and hard fibre-cement sheeting. The robot walked on each material in 25 different leg configurations to record the efficiency of its movement. We then tested its ability to automatically sense a surface change and choose the best body shape.

The real world is a much more variable and unpredictable place, though. We extended this method to unseen terrain by having the robot estimate the best body shape for any surface it encounters. In our outdoor experiments, DyRET used a machine learning model seeded with knowledge about leg configurations from the controlled tests. As it walks, it continuously predicts the best body shape for the terrain, while updating its model with measurements of how well it's actually moving. The predictions improve as it walks, allowing it to generate efficient movement even for terrain it hasn't seen before.

## Are shape-shifting robots the future?

DyRET explores the idea of "embodied cognition" — that a robot's hardware body can be used to solve problems in collaboration with its software brain, by tightly linking them to the environment. Instead of the body being a constraint on movement, it becomes an adaptive tool for solving problems in challenging environments.

This is especially valuable when we can't predict environmental conditions in advance, making it very hard to pick a single "good" robot shape. A shape-shifting robot can adapt to a wide variety of conditions through body change rather than having to be redesigned.

Our proof of concept has powerful implications for the future of robotic design, unlocking environments that are currently impossible to navigate. Future shape-shifting robots might be used on the sea floor, or for long-term missions in space.

---

This post is adapted from [an article David Howard and I wrote for *The Conversation*](https://theconversation.com/shape-shifting-robots-in-the-wild-the-dyret-robot-can-rearrange-its-body-to-walk-in-new-environments-157130). The research was carried out with Tønnes Nygaard, Jim Torresen, and Kyrre Glette at the University of Oslo, and David Howard at CSIRO's Data61.

This research is personally important as an impactful output from our EPEC (Engineering Predictability with Embodied Cognition) project at the University of Oslo. I spent 2016–2019 at UiO as a post-doc in the EPEC project and as one of Tønnes Nygaard's supervisors. It's so gratifying to see this robot go from barely-working initial concept in the lab to the subject of an international collaboration with a high-impact journal output in Nature Machine Intelligence.
