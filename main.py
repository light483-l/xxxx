from Samples.geocoder import geocode


def get_address_component(town, component_index):
    toponym = geocode(town)
    components = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]

    return components[component_index]["name"]


def main():
    for town in ["Хабаровск", "Уфа", "Нижний Новгород", "Калининград"]:
        province = get_address_component(town, 1)
        print(f"{town}: {province}")
    print("")


if __name__ == "__main__":
    main()