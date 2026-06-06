from ultralytics import YOLO


def train():

    model = YOLO("yolov8n.pt")

    model.train(
        data="data/helmet_dataset/data.yaml",
        epochs=50,
        imgsz=640,
        batch=8,
        workers=2,
        device="cpu"
    )


if __name__ == "__main__":
    train()