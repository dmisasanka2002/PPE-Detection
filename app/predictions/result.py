from utils.classes import classes

def get_result(yolo_result, selected_items):
    """
    Check if selected items are detected for each person.
    :param yolo_result: YOLO detection results.
    :param selected_items: List of selected items.
    :return: a massage if all selected items are detected for each person, otherwise a message and missing items.
    """
    detections_by_person = group_detections_by_person(yolo_result)
    for person, items in detections_by_person.items():
        missing_items = [item for item in selected_items if item not in items]
        if missing_items:
            return "PROCESSING COMPLETE. You ARE NOT ALLOWED TO ENTER.", missing_items
    return "PROCESSING COMPLETE. You CAN ENTER.", []

def group_detections_by_person(yolo_result):
    """
    Group detections by person.
    :param yolo_result: YOLO detection results.
    :return: Dictionary with persons as keys and detected items as values.
    """
    detections_by_person = {}
    for detection in yolo_result[0].boxes.data:
        class_id = int(detection[5])
        class_name = classes[class_id]
        if class_id == 6:  # Person class
            if class_name not in detections_by_person:
                detections_by_person[class_name] = set()
        else:
            for person in detections_by_person:
                detections_by_person[person].add(class_name)
    return detections_by_person
