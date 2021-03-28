import React from 'react';
import { View, Image } from 'react-native';
import { styles } from './styles';

const Menu = () => {
  return (
  <View style={styles.container} >
    <View style={styles.menu}>
      <Image styles={styles.textContainer} source={require('../../assets/right.png')} resizeMode='stretch' />
      <Image styles={styles.textContainer} source={require('../../assets/left.png')} resizeMode='stretch' />
    </View>
  </View>
    )
}

export default Menu;

