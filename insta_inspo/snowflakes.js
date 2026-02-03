const sketch = (p) => {
    p.snowSphere = null;

    p.setup = () => {
        p.cam = p.createCamera();
        p.cam.setPosition(0, 0, p.height / 2);

        p.snowSphere = new SnowSphere(p);
        p.rotationFunction = p.random(["rotateX", "rotateY", "rotateZ"]);
        p.rotationAmount = p.random([-0.005, 0.005]);

        const auroraGradient = p.generateAuroraBackground();
        p.createRegenerateButton();
    };
};