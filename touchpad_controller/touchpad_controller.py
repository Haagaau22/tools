import re
import subprocess


touchpad_id_regex = re.compile(r'↳(.*) Touchpad.*id=(\d+)\t\[')
touchpad_state_regex = re.compile(r'Device Enabled.*\t(\d)')


def get_touchpad_list():
    out_bytes = subprocess.check_output(['xinput', 'list'])
    result = []
    for line in out_bytes.decode('utf8').split('\n'):
        match_result = touchpad_id_regex.search(line)
        if match_result:
            # print(match_result.groups(0)[0], match_result.groups(0)[1], line)
            result.append((match_result.groups(0)[0], match_result.groups(0)[1]))
    return result


def get_touchpad_state(touchpad_id):
    state_map = {'0': False, '1': True}
    out_bytes = subprocess.check_output(['xinput', 'list-props', touchpad_id])
    for line in out_bytes.decode('utf8').split('\n'):
        match_result = touchpad_state_regex.search(line)
        if match_result:
            return state_map[match_result.groups(0)[0]]
    else:
        raise Exception('can\'t match touchpad state')

def control_touchpad():
    # touchpad_list = get_touchpad_list()
    for touchpad_name, touchpad_id in get_touchpad_list():
        touchpad_state = get_touchpad_state(touchpad_id)
        # print(touchpad_id, touchpad_name, touchpad_state)
        if touchpad_state is True:
            out_bytes = subprocess.check_output(['xinput', 'disable', touchpad_id])
            out_bytes = subprocess.check_output(['notify-send', f'触摸板{touchpad_name}关闭', '-i', '/usr/share/icons/Adwaita/48x48/devices/input-touchpad.png'])
        else:
            out_bytes = subprocess.check_output(['xinput', 'enable', touchpad_id])
            out_bytes = subprocess.check_output(['notify-send', f'触摸板{touchpad_name}打开', '-i', '/usr/share/icons/Adwaita/48x48/devices/input-touchpad.png'])

if __name__ == '__main__':
    control_touchpad()
    # print('touchpad list' ,get_touchpad_list())
