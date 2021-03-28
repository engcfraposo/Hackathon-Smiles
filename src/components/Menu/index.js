import React from 'react';
import { useNavigation } from '@react-navigation/native';
import { View, Image } from 'react-native';
import { RectButton } from 'react-native-gesture-handler';
import { styles } from './styles';

const Menu = () => {

const navigation = useNavigation();

  return (
  <View style={styles.container} >
    <View style={styles.menu}>
      <RectButton onPress={navigation.openDrawer()}>
      <Image styles={styles.textContainer} source={require('../../assets/right.png')} resizeMode='stretch' />
      </RectButton>
      <Image styles={styles.textContainer} source={require('../../assets/left.png')} resizeMode='stretch' />
    </View>
  </View>
    )
}

export default Menu;

