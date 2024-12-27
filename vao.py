from vbo import VBO
from shader_program import ShaderProgram

class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # cube vao
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cube'])

        # shadow cube vao
        self.vaos['shadow_cube'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['cube'])
        
        # road vao
        self.vaos['road'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['road'])
        
         # shadow road
        self.vaos['shadow_road'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['road'])
        
        # bench vao
        self.vaos['bench'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['bench'])
        
         # shadow bench
        self.vaos['shadow_bench'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['bench'])
        
         # garbagec vao
        self.vaos['garbagec'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['garbagec'])
        
         # shadow garbagec
        self.vaos['shadow_garbagec'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['garbagec'])
        
        # ctree vao
        self.vaos['ctree'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['ctree'])
        
         # shadow ctree
        self.vaos['shadow_ctree'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['ctree'])

        # skybox vao
        self.vaos['skybox'] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo=self.vbo.vbos['skybox'])

        # advanced_skybox vao
        self.vaos['advanced_skybox'] = self.get_vao(
            program=self.program.programs['advanced_skybox'],
            vbo=self.vbo.vbos['advanced_skybox'])

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()