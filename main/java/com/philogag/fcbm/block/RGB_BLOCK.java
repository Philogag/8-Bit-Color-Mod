package com.philogag.fcbm.block;

import com.philogag.fcbm.register.BlockRegister;

import net.minecraft.block.Block;
import net.minecraft.block.material.Material;
import net.minecraft.creativetab.CreativeTabs;

public class RGB_BLOCK extends Block {
//    public static Logger logger;
    public RGB_BLOCK(String name){
        super(Material.ROCK);
//        this.setBlockUnbreakable();
        this.setHardness(0.5F);
        this.setUnlocalizedName(name);
        this.setRegistryName(name);
        this.setCreativeTab(BlockRegister.tabBlock);

//        logger.info("Registe: " + name);
    }
}