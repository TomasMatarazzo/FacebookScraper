
def extract(url, driver, time):

    driver.get(url)
    information = {
        'link': url,
        'Title': '-',
        'Price': '-',
        'Profile': '-',
        'Description': '-',
        'Address': '-',
        'phone': '-',
        'email': '-'
    }
    # Searching the information for each item of the dic
    # Finding url
    information['link'] = url;
    time.sleep(2)

    # Finding the Title and price
    elements = driver.find_elements(By.CSS_SELECTOR, "div[class = '_59k _2rgt _1j-f _2rgt _3zi4 _2rgt _1j-f _2rgt'] ")
    information['Title'] = elements[0].text
    information['Price'] = elements[1].text
    time.sleep(2)

    # Finding the name of the profile

    parent = driver.find_elements(By.CSS_SELECTOR, "div[class = '_9_7 _2rgt _1j-f _2rgt']")
    parent = [e.text for e in parent if e.text != '']
    name = parent[5].split("\n")

    # In case it apppers a notification
    if name[0] == 'Seller Information':
        parent.pop(5)
    name = parent[5].split("\n")
    print(name)
    print('----')
    information['Profile'] = name[0]
    time.sleep(2)

    # Finding the description

    # This variable has all the information we will split to get better info
    data = parent[2]
    data = parent[2].split('\n')
    print(data)
    print('----')
    data = [data[i] for i in range(3, len(data))]
    time.sleep(2)

    # Description
    description = ' '.join(data)
    information['Description'] = description
    time.sleep(2)

    # Phone number
    for number in data:
        print(number)

    # Location
    time.sleep(2)
    location = driver.find_element(By.CSS_SELECTOR, "div[class = 'profileMapTile']")
    image = location.value_of_css_property('background-image')
    image = image[4:-1]

    return information
