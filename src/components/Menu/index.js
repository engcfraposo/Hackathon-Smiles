import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { Feather, FontAwesome } from '@expo/vector-icons';

const Menu = () => {
  return (
  <View style={styles.container} >
    <View style={styles.menu}>
      
    </View>
  </View>
    )
}

export default Menu;

const styles = StyleSheet.create({
  container: {
    width: '100%',
    paddingTop: 10,
    paddingHorizontal: 10,
    height: 90,
    backgroundColor: '#E48040',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
  },
  menu:{
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 10,
  },
  textContainer:{
    paddingHorizontal: 5,
  },
  titleLeftTop:{
    color: '#fff',
    textAlign: 'left',
  },
  titleLeftBottom:{
    color: '#fff',
    textAlign: 'left',
  },
  titleRightTop:{
    color: '#fff',
    textAlign: 'right',
  },
  titleRightBottom:{
    color: '#fff',
    textAlign: 'right',
  }
});